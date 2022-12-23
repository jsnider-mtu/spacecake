#!/usr/bin/env python3
# coding=utf-8
"""
This is a module for bot commands so that bot.py can import them.
Commands are if statements within functions. The ls tables let bot.py know that the command exists.

TODO
Clean up formatting
Add some comments (maybe)
Exception handling
"""
import json
import openai
import os
import random
import re
import time
import texas

texasgames = []

donger = ['ヽ〳 ՞ ᗜ ՞ 〵ง',
  's( ^ ‿ ^)-b',
  '(つ°ヮ°)つ  └⋃┘',
  '┬─┬ノ( ◕◡◕ ノ)',
  '╰( ◕ ᗜ ◕ )╯',
  'ଘ(੭*ˊᵕˋ)੭',
  'd–(^ ‿ ^ )z',
  '(つ°ヮ°)つ',
  '(> ^_^ )>',
  '☜(ﾟヮﾟ☜)',
  '┗(＾0＾)┓',
  '໒( ͡ᵔ ͜ʖ ͡ᵔ )७',
  '(ノ°▽°)ノ︵┻━┻',
  'ᕕ╏ ͡ ▾ ͡ ╏┐',
  '¯\_( ͠° ͟ʖ °͠ )_/¯',
  '(ᓄಠ_ಠ)ᓄ',
  'ʕง•ᴥ•ʔง',
  '(ง’̀-‘́)ง',
  '(งಠ_ಠ)ง',
  '༼⁰o⁰；༽',
  'ԅ⁞ ◑ ₒ ◑ ⁞ᓄ',
  '། – _ – །',
  '༼つಠ益ಠ༽つ ─=≡ΣO))',
  'ヽ(⌐■_■)ノ♪♬',
  '♪ヽ( ⌒o⌒)人(⌒-⌒ )v ♪',
  '♪O<( ･ ∀ ･ )っ┌iii┐',
  '[ ⇀ ‿ ↼ ]',
  'ヽ(”`▽´)ﾉ']

def PMFuncs(cmd, args, data, conn):
  chan = data['nick']
  print(cmd, chan)
  if cmd.lower() == 'openai_register':
    print('openai_register called')
    if len(args) != 0:
      if args[0] != '':
        conn.openai[chan] = args[0]
        openaijson = json.dumps(conn.openai)
        with open('/root/spacecake/openai.json', 'w') as f:
          f.write(openaijson)
        conn.say('Your openai api key has been stored.\n'\
                 'Use command .openai or !openai to talk '\
                 'to the AI chat bot.', chan)
      else:
        conn.say('Usage: /msg spacecake openai_register api_key', chan)
    else:
      conn.say('Usage: /msg spacecake openai_register api_key', chan)

def AddrFuncs(cmd, args, data, conn):
  chan = data['channel']
  if cmd.lower() == 'whohere':
    chan = args[0]
    msg = "Users in %s: %s %s" % (chan, ' '.join(conn.nicks[chan]), str(len(conn.nicks[chan])))
    print(msg)
  elif cmd.lower() == 'lastmessages':
    for row in conn.lastMsg:
      print("%s: %s" % (row, conn.lastMsg[row]))
  elif cmd.lower() == 'channels' and data['sender'] == conn.trusted:
    msg = "I'm in these channels: %s" % ' '.join(conn.channels)
    chan2 = conn.trusted.split('!')[0]
    conn.say(msg, chan2)
  elif cmd.lower() == 'slap':
    target = args[0]
    slappee = data['sender'].split('!')[0]
    if target in conn.nicks[chan]:
      msg = "slaps %s with a floppy fish, then points at %s" % (target, slappee)
    else:
      msg = "can't find %s" % target
    conn.describe(msg, chan)
  elif cmd.lower() == 'part' and data['sender'] == conn.trusted:
    chan = args[0]
    msg = ' '.join(args[1:])
    conn.leave(msg, chan)
  elif cmd.lower() == 'join' and data['sender'] == conn.trusted:
    chan = args[0]
    conn.join(chan)
  elif cmd.lower() == 'nick' and data['sender'] == conn.trusted:
    hancock = args[0]
    conn._send("NICK %s" % hancock)
  elif cmd.lower() == 'act' and data['sender'] == conn.trusted:
    chan = args[0]
    msg = ' '.join(args[1:])
    conn.describe(msg, chan)
  elif cmd.lower() == 'speak' and data['sender'] == conn.trusted:
    chan = args[0]
    if args[1] == 'to':
      to = args[2]
      msg = ' '.join(args[3:])
    else:
      msg = ' '.join(args[1:])
    if 'to' in locals():
      conn.say(msg, chan, to)
    else:
      conn.say(msg, chan)
  elif cmd.lower() == 'quit':
    asker = data['sender']
    if asker == conn.trusted:
      conn.quit('goodbye for now')
    else:
      conn.say('┌∩┐(ಠ_ಠ)┌∩┐', chan)
  elif cmd.lower() == 'die':
    conn.say('nou', chan)
  else:
    conn.say(random.choice(donger), chan)

def UnAddrFuncs(cmd, args, data, conn):
  chan = data['channel']
  sendNick = data['sender'].split('!')[0]
  if re.match('s/.+/.*/', cmd):
    pre = cmd.split('/')[1]
    suf = cmd.split('/')[2]
    if conn.lastMsg[sendNick]:
      msgre = conn.lastMsg[sendNick].replace(pre, suf)
      msg = "%s meant to say: %s" % (sendNick, msgre)
      conn.say(msg, chan)
    else:
      conn.say('i fucked up', chan)
  elif cmd.lower() == '!help' or cmd.lower() == '.help':
    conn.say("Help will be coming soon (but I don't promise)", chan)
  elif cmd.lower() == 'happy':
    if args[0].lower() == 'birthday' or args[0].lower() == 'bday':
      conn.say('♪O<( ･ ∀ ･ )っ┌iii┐', chan)
  elif cmd.lower() == 'donger' or cmd.lower() == 'dong' or cmd.lower() == 'smoak':
    conn.say(random.choice(donger), chan)
  elif cmd.lower() == '!flip' or cmd.lower() == '.flip':
    conn.say('(ノ°▽°)ノ︵┻━┻', chan)
  elif cmd.lower() == '!unflip' or cmd.lower() == '.unflip':
    conn.say('┬─┬ノ(°▽°ノ)', chan)
  elif cmd.lower() == '^5':
    fiver = data['sender'].split('!')[0]
    chan = data['channel']
    msg = "high fives %s in the face" % fiver
    conn.describe(msg, chan)
  elif cmd.lower() == 'o/':
    msg = "waves emphatically to %s" % sendNick
    msg2 = "Were you.. were you not waving at me?"
    msg3 = "sobs quietly in the corner"
    conn.describe(msg, chan)
    time.sleep(3)
    conn.say(msg2, chan)
    time.sleep(1.5)
    conn.describe(msg3, chan)
  elif cmd.lower() == '.openai' or cmd.lower() == '!openai':
    if data['sender'] == conn.trusted:
      openai.api_key = os.getenv('OPENAI_API_KEY')
    else:
      try:
        openai.api_key = conn.openai[data['nick']]
      except:
        conn.say('You need to register an api key to use this command\n'\
                 'To register: /msg spacecake openai_register api_key', chan)
    if openai.api_key != '':
      if len(args) != 0:
        try:
          response = openai.Completion.create(
            model='text-davinci-003',
            prompt=' '.join(args[0:]),
            temperature=0.5,
            max_tokens=200,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0.0
          )
          for res in response['choices'][0]['text'].split('\n'):
            if res != '':
              conn.say(sendNick + ': ' + res, chan)
        except openai.error.AuthenticationError:
          conn.say(sendNick + ': Your api key is invalid\nTry to register again', chan)
        except:
          conn.say(sendNick + ': Something unexpected went wrong', chan)
      else:
        conn.say('To register: /msg spacecake openai_register api_key\nUsage: .openai message', chan)
    else:
      conn.say(sendNick + ': Your api key is an empty string. Try to register again', chan)
  elif cmd.lower() == '.texas' or cmd.lower() == '!texas':
    if len(args) == 0:
      conn.say(".texas commands: newgame, list, join, start, bet, check, fold, hand, balance", chan)
      return
    texasplayers = []
    for z in texasgames:
      for a in z.table.seats:
        if a.isfilled():
          texasplayers.append(a.p.name)
    if sendNick not in texasplayers:
      if args[0].lower() == 'list':
        conn.say("Current games:", chan)
        for x in texasgames:
          curplayers = ""
          for y in x.table.seats:
            if y.isfilled():
              curplayers += f" {y.p.name}"
          conn.say(f"{x.name} -- Current players:{curplayers}", chan)
        return
      if args[0].lower() == 'newgame':
        if len(args) != 2:
          conn.say(sendNick + ": Usage: '.texas newgame <name>'", chan)
        else:
          for z in texasgames:
            if args[1] == z.name:
              conn.say(sendNick + f": The name {args[1]} is already taken", chan)
              return
          texasgames.append(texas.Game(args[1]))
          for z in texasgames:
            if z.name == args[1]:
              if z.playerjoin(texas.Player(sendNick)):
                conn.say(f"Texas Hold 'Em game {z.name} has been started by {sendNick}. Use '.texas join {z.name}' to join", chan)
              else:
                conn.say("Something went wrong starting a game (ノ°▽°)ノ︵┻━┻", chan)
      elif args[0].lower() == 'join':
        if len(args) != 2:
          conn.say(sendNick + ": Usage: '.texas join <name>'", chan)
        else:
          for z in texasgames:
            if args[1] == z.name:
              if z.playerjoin(texas.Player(sendNick)):
                conn.say(f"{sendNick} has joined the {z.name} Texas Hold 'Em game", chan)
                return
              else:
                conn.say(f"The {z.name} Texas Hold 'Em game is full, sorry {sendNick}", chan)
          conn.say(f"Game {args[1]} not found", chan)
      else:
        conn.say(sendNick + ": You aren't currently in a game. Use '.texas join <name>' to join a game", chan)
        conn.say("Or use '.texas newgame <name>' to start a new one", chan)
        conn.say("Current games:", chan)
        for x in texasgames:
          curplayers = ""
          for y in x.table.seats:
            if y.isfilled():
              curplayers += f" {y.p.name}"
          conn.say(f"{x.name} -- Current players:{curplayers}", chan)
    else:
      if args[0].lower() == 'newgame' or args[0].lower() == 'join':
        conn.say(sendNick + ": Must leave your current game before creating or joining a new one", chan)
        conn.say("'.texas quit' to leave your current game", chan)
      elif args[0].lower() == 'start':
        for x in texasgames:
          for y in x.table.seats:
            if y.isfilled():
              if y.p.name == sendNick:
                for z in x.table.seats:
                  if z.isfilled():
                    if z.p.purse < x.table.bigblind:
                      if x.playerleave(z.p):
                        conn.say(f"{z.p.name} has insufficient funds and has left the {x.name} table", chan)
                      else:
                        conn.say("Something went wrong in playerleave() (ノ°▽°)ノ︵┻━┻", chan)
                    else:
                      z.justsat = False
                if x.table.isready():
                  x.d.shuffle()
                  msg = x.blinds()
                  conn.say(msg)
                  for a in range(2):
                    for b in x.table.seats:
                      if b.isfilled():
                        if b.justsat == False:
                          x.d.deal(b.p)
                  a = x.dealer
                  for b in x.table.seats:
                    if b.isfilled():
                      if b.justsat == False and b.p.folded == False:
                        a += 1
                        if a == x.table.seatstaken():
                          a = 0
                        if a == (x.dealer + x.playerturn) % x.table.inplay():
                          conn.say(f"Player {b.p.name}'s turn. Current bet is ${x.table.pot.lastbet}", chan)
                          b.p.turn = True
                          if b.p.hasbet == False:
                            if x.table.pot.lastbet == 0:
                              b.p.minbet = 0
                            elif x.table.pot.lastbet >= b.p.purse:
                              b.p.minbet = b.p.purse
                            else:
                              b.p.minbet = x.table.pot.lastbet
                          elif b.p.lastbet < x.table.pot.lastbet:
                            b.p.minbet = x.table.pot.lastbet
                          else:
                            conn.say("Something wonky happened", chan)
                        else:
                          continue
                else:
                  conn.say(f"Not enough players to start game {x.name}", chan)
      elif args[0].lower() == 'quit':
        for x in texasgames:
          for y in x.table.seats:
            if y.isfilled():
              if y.p.name == sendNick:
                x.playerleave(y.p)
      elif args[0].lower() == 'bet':
        if len(args) != 2:
          conn.say(sendNick + ": Usage: '.texas bet <integer>' (floating point numbers will be truncated)", chan)
          return
        for x in texasgames:
          for y in x.table.seats:
            if y.isfilled():
              if y.p.name == sendNick and y.justsat == False and y.p.folded == False:
                try:
                  diff = int(args[1]) - y.p.lastbet
                  if int(args[1]) >= y.p.minbet:
                    if diff <= y.p.purse:
                      if y.p.bet(int(args[1]), diff):
                        x.table.pot.add(int(args[1]), diff)
                        conn.say(sendNick + f" has just bet ${int(args[1])}", chan)
                        x.playerturn += 1
                        a = x.dealer
                        for b in x.table.seats:
                          if b.isfilled():
                            if b.justsat == False and b.p.folded == False:
                              a += 1
                              if a == x.table.seatstaken():
                                a = 0
                              if a == (x.dealer + x.playerturn) % x.table.inplay():
                                if b.p.hasbet and b.p.lastbet == x.table.pot.lastbet:
                                  conn.say(f"Betting round over, current pot is ${x.table.pot.pot}", chan)
                                  if x.table.comm.flopcards == None:
                                    flopcardsmsg = "The Flop:"
                                    x.table.comm.flop()
                                    for c in x.table.comm.flopcards:
                                      flopcardsmsg += f" {c};"
                                    conn.say(flopcardsmsg, chan)
                                    conn.say(x.table.comm.cards(), chan)
                                    return
                                  elif x.table.comm.turncard == None:
                                    x.table.comm.turn()
                                    conn.say(f"The Turn: {x.table.comm.turncard}", chan)
                                    conn.say(x.table.comm.cards(), chan)
                                    return
                                  elif x.table.comm.rivercard == None:
                                    x.table.comm.river()
                                    conn.say(f"The River: {x.table.comm.rivercard}", chan)
                                    conn.say(x.table.comm.cards(), chan)
                                    return
                                  else:
                                    winners = x.calculatewinners()
                                else:
                                  conn.say(f"Player {b.p.name}'s turn. Current bet is ${x.table.pot.lastbet}", chan)
                                  b.p.turn = True
                                  if b.p.hasbet == False:
                                    if x.table.pot.lastbet == 0:
                                      b.p.minbet = 0
                                    elif x.table.pot.lastbet >= b.p.purse:
                                      b.p.minbet = b.p.purse
                                    else:
                                      b.p.minbet = x.table.pot.lastbet
                                  elif b.p.lastbet < x.table.pot.lastbet:
                                    b.p.minbet = x.table.pot.lastbet
                              else:
                                continue
                      else:
                        conn.say("Something went wrong in bet() (ノ°▽°)ノ︵┻━┻", chan)
                    else:
                      conn.say(sendNick + f": ${int(args[1])} is more than you have to bet (you have ${y.p.purse})", chan)
                  else:
                    conn.say(sendNick + f": ${int(args[1])} is less than the minimum bet of ${y.p.minbet}", chan)
                except ValueError:
                  conn.say(sendNick + f": {args[1]} is not an integer", chan)
      elif args[0].lower() == 'check':
        for x in texasgames:
          for y in x.table.seats:
            if y.isfilled():
              if y.p.name == sendNick and y.justsat == False and y.p.folded == False:
                if y.p.check():
                  conn.say(sendNick + " has just checked", chan)
                else:
                  conn.say(sendNick + f": you cannot check here, minimum bet is ${y.p.minbet}", chan)
      elif args[0].lower() == 'fold':
        for x in texasgames:
          for y in x.table.seats:
            if y.isfilled():
              if y.p.name == sendNick and y.justsat == False and y.p.folded == False:
                if y.p.fold():
                  conn.say(sendNick + " has just folded", chan)
                else:
                  conn.say("Something went wrong in fold() (ノ°▽°)ノ︵┻━┻", chan)
      elif args[0].lower() == 'hand':
        for x in texasgames:
          for y in x.table.seats:
            if y.isfilled():
              if y.p.name == sendNick and y.justsat == False and y.p.folded == False:
                conn.say(f"You have {y.p.hand} in your hand", sendNick)
                conn.say(f"Check your DMs {sendNick}", chan)
      elif args[0].lower() == 'balance':
        for x in texasgames:
          for y in x.table.seats:
            if y.isfilled():
              if y.p.name == sendNick:
                conn.say(sendNick + f" has a balance of ${y.p.purse}")

def OnJoinFuncs(channel, conn):
  pass

def OtherJoinFuncs(data, conn):
  chan = data['channel']
  if data['joiner'].split('!')[0] == 'redmagnus':
    conn.describe('drives circles around redmagnus while drinking a beer', chan)

def OnKickedFuncs(msg, data, conn):
  conn.channels.remove(data['channel'])

def OtherKickedFuncs(msg, data, conn):
  chan = data['channel']
  conn.say('╭∩╮ʕ•ᴥ•ʔ╭∩╮', chan)
