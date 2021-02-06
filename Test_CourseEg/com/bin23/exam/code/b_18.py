
class PlayGame:
    gameName = '王者荣耀'
    company = '腾讯公司'
    real_num = 0
    def __init__(self ,name ,HP ,attack ,skill):
        self.name = name
        self.HP = HP
        self.attack = attack
        self.skill = skill
        PlayGame.real_num += 1
    def action(self ,hero):
        import random
        import time
        while True:
            skill_hero = random.choice(hero.skill)
            skill_hero_index = hero.skill.index(skill_hero ) +1
            skill_self = random.choice(self.skill)
            skill_self_index = hero.skill.index(skill_self ) +1
            print("%s 受到了 %s 的%s技能攻击,受到伤害%d,%s剩余血量%d" %(
            self.name, hero.name, skill_hero, 30 * skill_hero_index, self.name, self.HP - 30 * skill_hero_index))
            self.HP -= 30 * skill_hero_index
            print("%s 反攻 %s ,使用%s技能攻击,造成伤害%d,%s剩余血量%d" % (
            self.name, hero.name, skill_self, 25 * skill_self_index, hero.name, hero.HP - 25 * skill_self_index))
            hero.HP -= 25 * skill_self_index
            time.sleep(0.5)
            print("=" * 80)
            if hero.HP <= 0:
                print('韩超战败了')
                return 1
            if self.HP <= 0:
                print('关羽战败了')
                return 0


print('产品介绍: %s 的 %s 游戏!' % (PlayGame.gameName, PlayGame.company))
print('比赛开始:-----------------------------------------------------', end='\n\n')
guanYu_skill = ['Q技能', 'W技能', 'E技能', 'R技能']
hanChaos_skill = ['Q技能', 'W技能', 'E技能', 'R技能']
guanYu = PlayGame('关羽', 1500, 100, guanYu_skill)
hanChao = PlayGame('韩超', 1200, 90, hanChaos_skill)
# hanChao.action(guanYu)
guanYu.action(hanChao)