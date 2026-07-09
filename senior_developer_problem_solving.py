import time

class MidLevelDeveloper:
    def __init__(self, name):
        self.name = name

    def solve_task(self, task_description):
        """Mid-level developers focus on executing defined tasks."""
        print(f"\n{self.name} (Mid-Level): Received task: '{task_description}'. Starting implementation.")
        # Simulate focused work on a specific task
        time.sleep(1)
        result = f"Task '{task_description}' completed successfully."
        print(f"{self.name} (Mid-Level): {result}")
        return result

class SeniorDeveloper:
    def __init__(self, name):
        self.name = name

    def analyze_problem(self, problem_description):
        """Senior developers analyze the root cause and broader impact."""
        print(f"\n{self.name} (Senior): Received problem: '{problem_description}'. Analyzing.")
        # Simulate deeper analysis, considering multiple factors
        time.sleep(2)
        root_cause = f"Root cause of '{problem_description}' identified: unexpected data format."
        impact = "Potential impact: data corruption in reporting module."
        print(f"{self.name} (Senior): {root_cause}")
        print(f"{self.name} (Senior): {impact}")
        return root_cause, impact

    def propose_solution(self, problem_description, root_cause, impact):
        """Senior developers propose holistic solutions, not just fixes."""
        print(f"{self.name} (Senior): Proposing solution for '{problem_description}'.")
        # Simulate designing a robust solution
        time.sleep(1.5)
        solution = f"Solution: Implement input validation layer and add automated tests for data integrity. This addresses '{root_cause}' and mitigates '{impact}'."
        print(f"{self.name} (Senior): {solution}")
        return solution

    def mentor_mid_level(self, mid_level_dev, task_description):
        """Senior developers guide and mentor others."""
        print(f"\n{self.name} (Senior): Mentoring {mid_level_dev.name} on task: '{task_description}'.")
        # Senior developer might guide the mid-level developer on how to approach it
        print(f"{self.name} (Senior): 'Focus on understanding the requirements thoroughly before coding.'")
        mid_level_dev.solve_task(task_description)

# --- Demonstration ---

# Mid-level developer's approach
mid_dev = MidLevelDeveloper("Alice")
mid_dev.solve_task("Implement user login feature")

# Senior developer's approach to a more complex issue
senior_dev = SeniorDeveloper("Bob")
root_cause, impact = senior_dev.analyze_problem("Intermittent data inconsistencies in reports")
solution = senior_dev.propose_solution("Intermittent data inconsistencies in reports", root_cause, impact)

# Senior developer mentoring a mid-level developer
senior_dev.mentor_mid_level(mid_dev, "Refactor database query for performance")
