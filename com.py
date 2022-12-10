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
import openai
import os
import random
import re
import time

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
  if cmd.lower() == 'openai_register':
    if len(args) != 0:
      if args[0] != '':
        conn.openai[chan] = args[0]
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
