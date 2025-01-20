print ('''
a
pirate
's treasure map
___
).x)
(:_(

Finrod

__________
/ \____;;___ \
         | / /
`.())oo().
     |\(% () * ^ ^ () ^ \
    % | | - % ------- |
%  \ | % )) |
%   \ | %________ |
         ejm97 %%%%

         {}
{}
\  _ - --_ /
\ /      \ /
| ()() |
\ + /
  ejm
96 / HHH \
/  \_ / \
    {}
{}
___________
___________) %{} %%%%%% /
              / {} %%%%%%%% / %% / %%%%%% /
              / %%\ %_ - --_ / \ / %%%%%% /
/ %%%% \ / / () | %%%%%% /
/ %%%%% | () / + / %%%%%% /
          / %%%%%%%\ + / HH %%\ %%%% /
/ %%%%%% / %HH / _ / %%%\ %%% /
ejm97 / %%%%%% / %%\ / %%%%%%{} % /
                             / %%%%% {} %%% /
                             /
                             /
                             /
                             /
                             / ''')
print ("Welcome to Treasure Island.\nyour mission is to  find the treasure.")
direction=input("Left  or right ")
if direction == "right" or direction == "Right":
    print("Game Over.")
elif direction == "Left" or direction == "left":
    direction1=input("Swim or Wait")
    if direction1 == "Swim" or direction1 == "swim":
        print("Game Over.")
    elif direction1 == "Wait" or direction1 == "wait":
        door=input("Which door ?")
        if door == "Blue" or door == "blue":
            print ("Game over")
        elif door == "Red" or door =="red":
            print("Game over")
        elif door == "Yellow" or door== "yellow":
            print ("You win the game congrats !")
