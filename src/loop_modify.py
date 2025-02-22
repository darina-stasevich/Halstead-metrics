def modify_loop_counts(operators):
    if operators.get('for'):
        operators['()'] -= operators['for']

    # do ... while
    if operators.get('do'):
        count_do = operators['do']
        operators['while'] -= count_do
        if count_do:
            operators['do ... while'] = count_do

    # for ... of
    if operators.get('of'):
        count_of = operators['of']
        operators['for'] -= count_of
        if count_of:
            operators['for ... of'] = count_of

    # for ... in
    if operators.get('in'):
        count_in = operators['in']
        operators['for'] -= count_in
        if count_in:
            operators['for ... in'] = count_in
