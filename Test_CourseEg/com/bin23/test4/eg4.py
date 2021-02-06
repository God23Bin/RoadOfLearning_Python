job_year = int(input("请输入入职年限"))
list_award = []

while job_year != -1 and job_year >= 0:
    sell_achievement = eval(input("请输入销售业绩"))
    if job_year > 5:
        if sell_achievement > 15000:
            award_proportion = 0.2
        elif sell_achievement > 10000:
            award_proportion = 0.15
        elif sell_achievement > 5000:
            award_proportion = 0.1
        else:
            award_proportion = 0.05
    else:
        if sell_achievement > 4000:
            award_proportion = 0.045
        else:
            award_proportion = 0.01
    award = sell_achievement * award_proportion
    print("奖金比例:", award_proportion)
    print("奖金:", award)

    list_award.append(award)
    job_year = int(input("请输入入职年限"))

print(list_award)
