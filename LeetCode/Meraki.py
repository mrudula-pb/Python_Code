# Problem Statement:
'''#We have a Support Escalation System which is used by Customers to file any issues or support request. #During the course of issue/support request resolutions many departments are involved and issues pass through #multiple departments.

#Each issue starts with the state "Submitted" and goes through certain state during the workflow and it can #remain in only one state at given point in time and can only change it's state sequentially.

#Create a State Machine Validator where a state of an object starts with a particular state because of an #event or input and advances to the next stage in a sequential manner. An object can remain in only one #finite-state at any given time. For example:

#Support Escalation System:
#Submitted → Escalated → Reviewed → Approved → Deployed → Closed

#Exercise:
#For given list of Strings which defines different state for one of the above example. please write a #script/program to validate that each string is in following the defined state transition model.
#This State Validation program will be used to check each Support Request has proper sequential transition. #You are given the valid sequence of states.

#For example
#{Submitted, Reviewed, Reviewed, Approved, Deployed, Closed}
#{Submitted, Escalated, Reviewed}                           - VALID
#{Submitted, Escalated, Reviewed, Approved, Deployed}       - VALID
#{Submitted, Escalated, Reviewed, Approved, Deployed, Closed}       - VALID
#{Submitted, Escalated, Deployed}                           - INVALID
#{Submitted, Escalated, Approved, Deployed}                 - INVALID
'''


def check_states(different_states, ordered_states):
    i = 0
    for state in different_states:
        for
            if state == 'Submitted':

        '''if different_states[i] == 'Submitted':
            i += 1
            if different_states[i] == 'Escalated':
                i += 1
                if different_states[i] == 'Reviewed':
                    i += 1
                    if different_states[i] == 'Approved':
                        i += 1
                        if different_states[i] == 'Deployed':
                            i += 1
                            if different_states[i] == 'Closed':
                                return True
            else if:'''


def main():
    different_states = ['Submitted', 'Escalated', 'Reviewed']
    ordered_states = ['Submitted', 'Escalated', 'Reviewed', 'Approved']
    check_State = check_states(different_states)

    print("Checking States:", check_State)


if __name__ == '__main__':
    main()