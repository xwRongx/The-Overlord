'''
   *************************************
    Project: The Overlord（ΦωΦ）
    Names of Partners: Rose Wong and Anika Sivadalla
    （ΦωΦ）（ΦωΦ）（ΦωΦ）（ΦωΦ）（ΦωΦ）
   *************************************
'''

def story():
  name = input('What is your name? ✯ ')
  
  #first branch; 3 choices- choice 1 is the only interesting one though
  print (name + ''', you spill milk on yourself. You are able to rewind time once in your life. Do you use it or not（ΦωΦ）? Press 1 for choice 1 or 2 for choice 2.

  1. press 1 if you want to use it
  2. press 2 if you want to continue with your life
  3. other''')

  # time_loop variable stores the choice of the player
  time_loop = input('✯ ')

  #repeat is the variable that will decide when the while loop ends
  repeat = True

  #as long as the player does not get to a branch where repeat = False, the loop will continue
  while repeat == True:
    
    #second branch; if the first option to the previous branch was chosen, player enters time loop that only has one ending
    if time_loop == '1':
      print ('''You just wake up（ΦωΦ）. Do you choose the blue shirt or red shirt?
      
      1. red shirt
      2. blue shirt
      3. askjdfkjwe''')

      shirt = input('✯ ')

      # dead end, loops back to first if statement
      if shirt == '1':
        print('Your cat（ΦωΦ） isn\'t interested in you so you feel sad. You spill your milk because of absentmindedness. You are in a bad mood all day.K̵̡̹̱͒̓I̷̠̋̎̋͝T̶͔̈́̀Ṱ̵̑͊Y̶̛̼̰͙͕̭̳̗̫̺̑͐̌͐͜ ̷̢̛̱͍̺̣̠̲̒̏͜ͅI̶̱̖̥̜̘̬̭̬̫͐̍̏̂͑̌̚͜Ş̸̘̱̪͆͂̓͆̔̓̚ ̴̧̛̭̲̗̤͈̥̾͛͐̅̋̐͜A̵̺̥̔N̶̛͍̜̻̘̲̠̼̅̈́͘͠G̵̣̲͈̯̰̮̀R̶̪̦͇̗̯̲͔͐̅͂̔͠. You loop back to waking up.')
        
      #third branch; last branch in while loop
      elif shirt == '2':
        print('''Your cat（ΦωΦ）comes by, rubbing its head against your leg and meowing. Do you pet the cat （ΦωΦ）or not?
        
        1. pet kitty（ΦωΦ） like a lowly slave should do
        2. deny the overlord（ΦωΦ）of her majesty's headpats
        3. jfksjlfa''')

        kitty = input('✯ ')
        
        #This is the only ending to the first if statement
        if kitty == '1':
          print('Kitty（ΦωΦ） is satisfied with your lowly offerings. You shall be set free.')

          repeat = False
      
        # dead end, loops back to first if statement
        elif kitty == '2':
          print('The O̶v̶e̶r̶l̶o̶r̶d̶ kitty（ΦωΦ） gets angry and scratches your hand because it wants attention. You spill your milk again. You are in a bad mood all day.T̸̜̯͔̯̹̱̲̮̆̚H̶͖͒͐̕Ȅ̵̡̡̛̟̩̲̜̈́̋̎̀̅̃̌͘ͅ ̸̤̦͌̅͝O̵͓͎͙̻̰̿̽̀̇͊̉͗̚V̵̛̟͐Ë̸̢̻͕̰̲̻R̵̽̅ͅL̸͍͈̳̻̣̮̰͑O̵̧͓̣͕͖̗̔̚R̷͎̖̱̥͙̲̤̬̰͕͐̎͒D̷̢̧͓̱͔̠̟͕͊͌͐̎̆̃͐̔͊̑ ̶͓̱̙̖͗̊͐͌̂͊̍̓͛Ḯ̶̻̜̲̲̪̩̋͂͒̀̒̓̉̈́̍S̶̺͔̗̠̙͊̽ ̵̹͉̗̏Ḑ̷͔̜̱̪̲̀͐I̸̢͉̹̘̖̝̗͙͔̘͂̈́́̍̈́̃͊̀͘͝S̸̟̜̫̭͊̈́̆͜͠P̷̟̙̼̳̜͙̯̹̼̈́L̷͇͚͉͒̈́͌̾̊̕͘E̶͚̣̮̍̈́͆̉̽̈̄̚A̶̟̠̮͛̒̿̐͛͆̊̕͝S̸̥̭̣̖̼̳̝͈͙̦͊͋̋͝Ę̶͙̘͓̙̇̅̒Ḑ̸͚̝̐́͗̋̍ You loop back to waking up.')
      
        # dead end, loops back to first if statement
        else: 
          print('Kitty （ΦωΦ）demands headpats! Kitty （ΦωΦ）demands tribute!Ṣ̵̦̠̫͉̮͚̙̀̔̋͋̎̂̊̍̑U̵͓͖̼͋͠B̵̧̤̼͓͒M̷̮͎̦̼̪̹͎̪͗̇͆̀͐̀̌̚͘Į̶̨̛͖̲͉̝̬͕̫̒̀͑́̆͗̉̎T̵̛̰̍̄͐͒͐̋̑̅ͅ ̴͉̫̹̈́̑͐̄̽̉̂ͅŢ̶͕̫̙̬͓̠͚̈́̉͛Ó̵̩̍̽̿͛̎͘͝ ̶̘̱̗̻̲̼͍̦͛͗̋̉̊̕͜T̶͖̏Ḩ̵̨̨͍̰̼̈̀Ḙ̷̬̜̈́͛̍̌́̂͠͝͠ ̷̘͖̟͊͊Ỡ̴̙͍̯͙͙͗́̅̓͘V̷̨͖̭̳͔̀́̎̀Ë̷̤̞͙́̽͊̐͛͗͠R̷̟͕̺̉͂̚͝Ļ̵͙͇̠͍̟̲́͋̈́̇̃͠͝͝ͅO̷̯͔͑̂̑̅̔̃̕A̴̢̡͚͓̽̊̆́́̚A̶̺͑̅̏͂̊̈́̊R̶̡̝͖̼͚̺͈̒̽͑̆̇̊͋͆D̷̬̺̝͈̜̣̲͆̋͋̀͜D̷̝̝̘̗͖̙̗̯̦͐͒͐͗̐̒͐͠D̶̨̨͈̫͎͚͙͉͉̱̋̊͘D̵̗̳͓̯̒̍̍̎͊̎（ΦωΦ）')

      # dead end, loops back to first if statement
      else:
        print('Paralyzed by indecision, you stand there like a statue for the rest of your life.')

    #option 2 ends the program with some foreshadowing to encourage the player to try again
    elif time_loop == "2":
      print('''You continue on with your life with a bad mood all day and develop depression. （ΦωΦ）ಠ益ಠ   T̶̹͒̄̍̽̎̃̅͠H̷̨̧̖̦͔̹̅̍̆̿̊̈́̋͛͝Ę̸͖̟̙͓̿̿̔́̓͌́͠ ̷̧̙̮̰̜̝̘̭͋̀̀͂̎̍̅̄͠͠O̵͉̠͉̹͒̾V̸̡̨̨̲̘͉̜̉̃̌͜͝Ê̶͔̗̺Ŗ̵̨̥̖̝͎̲̤́̾̔̈́̕ͅL̷̹̼̹͈̪̘̦̔̎̂̉́̒̎̽͑̓O̸̥͖͍̯̞̹̓̑͑̋̐̈́͌À̵͚̼̖͖͖̜͔̭̀̍̀̒̄́̽̚R̸̫̝͎̊̌̌͒̚D̸̛͈̈̂̈́̈ ̶̬̜̯̓̑̑́̈́͂̚͜I̵̠̬͖̞̠͔͐̍̾́̂̐̑͠Ş̶̟̼͇͍̦̦̟͛̏̿͝ ̸̞͕͔̰̈́̕A̴̛̞̺̞̯̍͗͊̈́̉̕͝N̵̨̛̦̮̤̩̩̹̟̼̥G̵̻̻̩̻̫̦͚̗͐̃̇̏͊̔̃͠R̸͎̭̠͓͚̹̪͚͈̔͗͜͝Y̵̛͑̑s͉̭͇̱͛̆͛̌̾̕͝Ÿ̴̰̥͎̂̊̆̈̌̑͗͘Y̵̝̗̱̏͋̈́͂Ȳ̷̻̩͆͌̈́̑͊͗Ỵ̷̢̛͚͉̳͍̋̿̅Ū̶̧̢͍͒̀̏̑̽̒͒̈͋
      ̢t̢r̢̢i̢ agen''')
      repeat = False

    #Pressing anything else also ends the program, but in a more cryptic way
    else:
      print ('You freak out and faint.')
      ask = input('Now you can\'t do anything（ΦωΦ）✯ ')
      print('（ΦωΦ）ಠ益ಠ)triagen')
      repeat = False

#this calls the function
story()











