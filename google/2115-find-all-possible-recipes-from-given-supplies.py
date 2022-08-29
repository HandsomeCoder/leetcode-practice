from collections import defaultdict, deque
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
		
        rln = len(recipes)
        in_degree = {recipes[idx] : len(ingredients[idx]) for idx in range(rln)}

        for idx in range(rln):
            for item in ingredients[idx]:
                graph[item].append(recipes[idx])
		
        queue = deque(supplies)

        result = []
        while queue:
            itr = queue.popleft()
            for item in graph[itr]:
                in_degree[item] -= 1
                if in_degree[item] == 0:
                    queue.append(item)
                    result.append(item)
	
        return result        