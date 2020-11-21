import copy
import numpy as np
import random

class MaruBatuGame:
    
    def __init__(self):
        
        #〇と✖が３つ並んだときの状況を先に設定
        maru_goal = [
            [1,1,1, 0,0,0, 0,0,0],
            [0,0,0, 1,1,1, 0,0,0],
            [0,0,0, 0,0,0, 1,1,1],
            [1,0,0, 1,0,0, 1,0,0],
            [0,1,0, 0,1,0, 0,1,0],
            [0,0,1, 0,0,1, 0,0,1],
            [1,0,0, 0,1,0, 0,0,1],
            [0,0,1, 0,1,0, 1,0,0]
        ]
        
        batu_goal = copy.deepcopy(maru_goal)
        li_index1 = 0
        for maru_li in maru_goal:
            li_index2 = 0
            for i in maru_li:
                if i == 1:
                    batu_goal[li_index1][li_index2] = -1
                li_index2 += 1
            li_index1 += 1
        
        #〇と✖が３つのとき（ゴール）のインスタンスを生成
        self.maru_goal = maru_goal
        self.batu_goal = batu_goal
        #〇を1とする
        self.maru = 1
        #✖を-1とする
        self.batu = -1
        #〇と✖を何も置いていないリストを作成(今後3×3の盤面に変更する)
        self.check_list = [0,0,0, 0,0,0, 0,0,0]
       
    def cheak_goal(self):
        flag_mark = 0
        for mark in [self.maru, self.batu]:
            if mark == 1:
                goal_cluster = self.maru_goal
            else :
                goal_cluster = self.batu_goal

            for goal_li in goal_cluster:
                count = 0
                #何個並んでいるか確認
                line_count = 0
                for i in goal_li:
                    if i == mark:
                        if self.check_list[count] == mark:
                            line_count +=1
                    count += 1
                if 3 <= line_count:
                    flag_mark = mark
                    break
                else:
                    pass
        return flag_mark
    
    
    #1×9の盤面を3×3の盤面に変える
    def make_table(self):

        #〇✖ゲームは3×3の盤面のゲーム blank = 0
        table = np.zeros((3, 3)).astype(int)

        count = 0
        li_index1 = 0
        li_index2 = 0

        for i in self.check_list:
            table[li_index1][li_index2] = i
            li_index2 += 1
            count += 1
            if count % 3 == 0:
                li_index1 += 1
                li_index2 =  0
        return table
    
    
    def display(self, table):  
        for y in range(3):
            for x in range(3):
                if table[x][y] == self.maru:
                    print('○', end = '  ')
                elif table[x][y] == self.batu:
                    print('✖', end = '  ')
                else:
                    print('・', end = '  ')
            print('\n', end = '')
            
              
    def play(self):
        print(f"###スタート###")
        count = 0
        while True:
            self.display(self.make_table())
            print(f"###{count+1}ターン目###")

            flag = self.cheak_goal()
            
            if flag== 1 :
                print("############")
                print("〇の勝ち")
                print("")
                self.display(self.make_table())
                break

            elif flag == -1:
                print("############")
                print("✖の勝ち")
                print("")
                self.display(self.make_table())
                break

            # すべて置いたら引き分けで終了
            if 0 not in self.check_list: 
                print("############")
                print("引き分け")
                print("")
                self.display(self.make_table())
                break

            if count% 2 == 0:
                mark = self.maru 
            else:
                mark = self.batu

            # 置ける場所を探す
            w = [i for i in range(len(self.check_list)) if self.check_list[i] == 0]
            # ランダムに置いてみる
            r = random.choice(w)
            self.check_list[r] = mark
            
            count += 1

maru_batu_game = MaruBatuGame()
maru_batu_game.play()