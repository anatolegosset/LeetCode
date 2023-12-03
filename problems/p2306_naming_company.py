class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        by_prefix = {}
        for idea in ideas:
            if idea[0] not in by_prefix:
                by_prefix[idea[0]] = set()
            by_prefix[idea[0]].add(idea[1:])
        nb_ideas = len(ideas)
        result = nb_ideas * (nb_ideas - 1)
        ideas.sort(key=lambda x: x[1:])
        previous_suffix = ''
        lead_set = set()
        for idea in ideas:
            suffix = idea[1:]
            lead = idea[0]

            if suffix == previous_suffix:
                lead_set.add(lead)
            else:
                previous_suffix = suffix
                if len(lead_set) > 1:
                    result -= (len(lead_set) - 1) * (2 * sum([len(by_prefix[char]) for char in lead_set]) - len(lead_set))
                lead_set = {lead}
        if len(lead_set) > 1:
            result -= (len(lead_set) - 1) * (2 * sum([len(by_prefix[char]) for char in lead_set]) - len(lead_set))

        result -= sum([len(by_prefix[char]) * (len(by_prefix[char]) - 1) for char in by_prefix])

        possible_leads = list(by_prefix.keys())

        for i in range(1, len(possible_leads)):
            for j in range(i):
                nb_hits = len(by_prefix[possible_leads[i]].intersection(by_prefix[possible_leads[j]]))
                result += 2 * nb_hits * (nb_hits - 1)

        return result

