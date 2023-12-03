class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        nb_skills = len(req_skills)
        old_subset_dict = {}
        for i, p in enumerate(people):
            bitmask = 0
            p_skills = set(p)
            for req_skill in req_skills:
                bitmask = bitmask << 1
                if req_skill in p_skills:
                    bitmask += 1
            if bitmask.bit_count() == nb_skills:
                return [i]

            flag = True
            for previous_p in list(old_subset_dict.keys()):
                if (previous_p & bitmask) == bitmask:
                    flag = False
                    break
                if (previous_p & bitmask) == previous_p:
                    del old_subset_dict[previous_p]
            if flag:
                old_subset_dict[bitmask] = [i]
        people = [0] * len(people)
        for k, v in old_subset_dict.items():
            people[v[0]] = k

        pp_map = []
        filtered_people = []
        for i, bitmask in enumerate(people):
            if bitmask:
                old_subset_dict[bitmask] = [len(pp_map)]
                pp_map.append(i)
                filtered_people.append(bitmask)
        nb_people = len(filtered_people)

        while True:
            subset_dict = {}
            for previous_bitmask in old_subset_dict:
                for i in range(old_subset_dict[previous_bitmask][-1] + 1, nb_people):
                    new_bitmask = previous_bitmask | filtered_people[i]
                    if new_bitmask.bit_count() == nb_skills:
                        old_subset_dict[previous_bitmask].append(i)
                        return [pp_map[j] for j in old_subset_dict[previous_bitmask]]
                    if new_bitmask != previous_bitmask and new_bitmask not in old_subset_dict:
                        new_pp = list(old_subset_dict[previous_bitmask])
                        new_pp.append(i)
                        subset_dict[new_bitmask] = new_pp
            old_subset_dict = subset_dict



