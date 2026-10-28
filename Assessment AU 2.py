# One day the manager at a fintech company decides to create a team for the next project. There are a total of n employees and the skill-level of ith employee is Ai. 



# He thinks that the more employees a project has, the easier it gets to work and the project would be finished in fewer days. So he decides to create a team with the maximum number of employees possible. But there must be a balance factor within the team, so the manager decides to create a team in such a way that the skill-level of each pair of employees within the team would differ by no more than 5. 



# Your task is to help the manager find the maximum number of employees that could be accommodated in the team.



# Example 1:

# Input: n=8, A= [4, 17, 8, 24, 6, 10, 12, 9]
# Output: 4
# Explanation: In the example above,  there can be a maximum of 4 members in the team, the team can comprise of employees with skill-level 4 8 6 9, i.e, employees with indices 1, 3, 5, 8.


# Example 2:

# Input: n=6, A =[1,  10,  17,  12,  15,  2]
# Output: 3
# Explanation:  The manager can create a team with skills  [17, 12, 15].


# Constraints

# 1 ≤ n ≤ 10^4
# 1 ≤ Ai ≤ 10^9


//sliding window
def max_team(n, A):
    A.sort()
    left = 0
    max_count = 0

    for right in range(n):
        while A[right] - A[left] > 5:
            left += 1

        max_count = max(max_count, right - left + 1)

    return max_count


n = 8
A = [4, 17, 8, 24, 6, 10, 12, 9]
print(max_team(n, A))  # Output: 4
