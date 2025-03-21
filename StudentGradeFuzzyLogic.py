

import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

attendance = ctrl.Antecedent(np.arange(0, 101, 1), 'attendance')
marks = ctrl.Antecedent(np.arange(0, 101, 1), 'marks')
assignments = ctrl.Antecedent(np.arange(0, 101, 1), 'assignments')
final_grade = ctrl.Consequent(np.arange(0, 101, 1), 'final_grade')

attendance['low'] = fuzz.trimf(attendance.universe, [0, 0, 50])
attendance['medium'] = fuzz.trimf(attendance.universe, [40, 50, 60])
attendance['high'] = fuzz.trimf(attendance.universe, [50, 100, 100])

marks['low'] = fuzz.trimf(marks.universe, [0, 0, 40])
marks['medium'] = fuzz.trimf(marks.universe, [30, 50, 70])
marks['high'] = fuzz.trimf(marks.universe, [60, 100, 100])

assignments['low'] = fuzz.trimf(assignments.universe, [0, 0, 30])
assignments['medium'] = fuzz.trimf(assignments.universe, [20, 50, 80])
assignments['high'] = fuzz.trimf(assignments.universe, [70, 100, 100])

final_grade['low'] = fuzz.trimf(final_grade.universe, [0, 0, 50])
final_grade['medium'] = fuzz.trimf(final_grade.universe, [40, 50, 70])
final_grade['high'] = fuzz.trimf(final_grade.universe, [60, 100, 100])


plt.figure(figsize=(12, 8))

plt.subplot(2,2,1)
plt.plot(attendance.universe, attendance['low'].mf, label='Low Attendance')
plt.plot(attendance.universe, attendance['medium'].mf, label='Medium Attendance')
plt.plot(attendance.universe, attendance['high'].mf, label='High Attendance')
plt.title("Attendance")
plt.xlabel("Attendance Percentage")
plt.ylabel("Membership Function")
plt.legend()

plt.subplot(2,2,2)
plt.plot(marks.universe, marks['low'].mf, label='Low Marks')
plt.plot(marks.universe, marks['medium'].mf, label='Medium Marks')
plt.plot(marks.universe, marks['high'].mf, label='High Marks')
plt.title("Marks")
plt.xlabel("Marks Percentage")
plt.ylabel("Membership Function")
plt.legend()

plt.subplot(2,2,3)
plt.plot(assignments.universe, assignments['low'].mf, label='Low Assignments')
plt.plot(assignments.universe, assignments['medium'].mf, label='Medium Assignments')
plt.plot(assignments.universe, assignments['high'].mf, label='High Assignments')
plt.title("Assignments")
plt.xlabel("Assignments Percentage")
plt.ylabel("Membership Function")
plt.legend()

plt.tight_layout()
plt.show()

rules = [
    ctrl.Rule(attendance['low'] & marks['low'] & assignments['low'], final_grade['low']),
    ctrl.Rule(attendance['low'] & marks['medium'] & assignments['low'], final_grade['low']),
    ctrl.Rule(attendance['low'] & marks['high'] & assignments['low'], final_grade['medium']),

    ctrl.Rule(attendance['medium'] & marks['low'] & assignments['low'], final_grade['low']),
    ctrl.Rule(attendance['medium'] & marks['medium'] & assignments['low'], final_grade['medium']),
    ctrl.Rule(attendance['medium'] & marks['high'] & assignments['low'], final_grade['medium']),

    ctrl.Rule(attendance['high'] & marks['low'] & assignments['low'], final_grade['low']),
    ctrl.Rule(attendance['high'] & marks['medium'] & assignments['low'], final_grade['medium']),
    ctrl.Rule(attendance['high'] & marks['high'] & assignments['low'], final_grade['medium']),

    ctrl.Rule(attendance['high'] & marks['high'] & assignments['high'], final_grade['high']),
    ctrl.Rule(attendance['high'] & marks['high'] & assignments['medium'], final_grade['high']),
    ctrl.Rule(attendance['medium'] & marks['medium'] & assignments['medium'], final_grade['medium']),
    ctrl.Rule(attendance['low'] & marks['low'] & assignments['medium'], final_grade['low']),
    ctrl.Rule(attendance['medium'] & marks['high'] & assignments['medium'], final_grade['medium']),
    ctrl.Rule(attendance['high'] & marks['medium'] & assignments['high'], final_grade['high']),
]

grade_ctrl = ctrl.ControlSystem(rules)
grade_sim = ctrl.ControlSystemSimulation(grade_ctrl)

grade_sim.input['attendance'] = 50
grade_sim.input['marks'] = 50
grade_sim.input['assignments'] = 50

grade_sim.compute()

print("Final Grade: ", grade_sim.output['final_grade'])
final_grade.view(sim=grade_sim)

