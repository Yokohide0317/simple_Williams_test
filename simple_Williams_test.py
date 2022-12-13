

def get_mean(_df, _group, _label, _label_col):
    t = _df[_df[_label_col] == _group][_label].sum()
    n = len(_df[_df[_label_col] == _group][_label])
    return t / n


def continue_bigger_smaller(_df, _label, _group_list, _group_col, bigger=True):
    for i in range(len(_group_list)-1):
        targets = _group_list[i:i+2]
        tar1 = get_mean(_df, targets[0], _label, _group_col)
        tar2 = get_mean(_df, targets[1], _label, _group_col)
        if bigger == True:
            if tar1 > tar2:
                return False
        else:
            if tar1 < tar2:
                return False
    return True


def will_test(_df, _group_list, _group_col):
    result = []

    columns = _df.copy().drop(_group_col, axis=1).columns
    for label in columns:
        if continue_bigger_smaller(_df, label, _group_list, _group_col, bigger=True) or continue_bigger_smaller(_df, label, _group_list, _group_col, bigger=True):
            result.append(label)

    return result

if __name__ == "__main__":

    # {{{ Create Test DataFrame
    import pandas as pd
    test_data = {
        1: [1, 4, 8, 9],
        2: [2, 2, 9, 2],
        3: [3, 5, 14, 3],
        4: [4, 3, 14, 2],
        5: [5, 1, 15, 8],
        6: [2, 1, 13, 2],
    }
    df = pd.DataFrame(test_data).T

    label = [
        "30sec",
        "1min",
        "2min",
        "3min",
        "4min",
        "30sec"
    ]

    df = df.assign(label=label)
    df.columns = ["Mr.A", "Mr.B", "Ms.C", "Mrs.D", "label"]

    """ ex
        Mr.A	Mr.B	Ms.C	Mrs.D	label
    1	1	    4	    8	    9	    30sec
    2	2	    2	    9	    2	    1min
    3	3	    5	    14	    3	    2min
    4	4	    3	    14	    2	    3min
    5	5	    1	    15	    8	    4min
    6	2	    1	    13	    2	    30sec
    """
    # }}}


    label_list = ["30sec", "1min", "2min", "3min", "4min"]
    label_col_name = "label"
    result = will_test(df, label_list, label_col_name)
    print(result)


