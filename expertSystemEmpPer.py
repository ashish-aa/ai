class Employee:
    def __init__(self, name):
        self.name = name
        self.criteria = {}

    def set_criteria(self, criteria, score):
        self.criteria[criteria] = score

    def get_criteria(self):
        return self.criteria


class PerformanceEvaluation:
    def __init__(self):
        # Define evaluation criteria
        self.criteria_list = ["Work Quality", "Teamwork", "Punctuality", "Problem-Solving", "Communication"]
        self.evaluation_rules = {
            "Excellent": lambda scores: all(score >= 8 for score in scores.values()),
            "Good": lambda scores: all(score >= 6 for score in scores.values()),
            "Average": lambda scores: all(score >= 4 for score in scores.values()),
            "Needs Improvement": lambda scores: any(score < 4 for score in scores.values()),
        }

    def evaluate(self, employee):
        scores = employee.get_criteria()

        for level, rule in self.evaluation_rules.items():
            if rule(scores):
                return level
        
        return "Unknown"

    def generate_report(self, employee):
        evaluation = self.evaluate(employee)
        report = f"Performance Evaluation Report for {employee.name}:\n"
        report += f"Overall Evaluation: {evaluation}\n"

        for criteria, score in employee.get_criteria().items():
            report += f"{criteria}: {score}/10\n"

        return report


# Example usage
if __name__ == "__main__":
    # Create an employee
    employee = Employee("John Doe")

    # Set performance criteria scores
    employee.set_criteria("Work Quality", 9)
    employee.set_criteria("Teamwork", 8)
    employee.set_criteria("Punctuality", 7)
    employee.set_criteria("Problem-Solving", 8)
    employee.set_criteria("Communication", 7)

    # Evaluate performance
    evaluator = PerformanceEvaluation()
    report = evaluator.generate_report(employee)

    # Print the performance evaluation report
    print(report)
