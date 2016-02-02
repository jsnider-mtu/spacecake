#!/usr/bin/env python
# coding=utf-8
"""
This is a module for bot commands so that bot.py can import them.
Commands are if statements within functions. The ls tables let bot.py know that the command exists.
"""
import cleverbot
import random
import re

trusted = 'josh1238!~josh1238@unaffiliated/josh1238'
donger = ['ヽ〳 ՞ ᗜ ՞ 〵ง'.decode('utf-8'),
  's( ^ ‿ ^)-b'.decode('utf-8'),
  '(つ°ヮ°)つ  └⋃┘'.decode('utf-8'),
  '┬─┬ノ( ◕◡◕ ノ)'.decode('utf-8'),
  '╰( ◕ ᗜ ◕ )╯'.decode('utf-8'),
  'ଘ(੭*ˊᵕˋ)੭'.decode('utf-8'),
  'd–(^ ‿ ^ )z'.decode('utf-8'),
  '(つ°ヮ°)つ'.decode('utf-8'),
  '(> ^_^ )>'.decode('utf-8'),
  '☜(ﾟヮﾟ☜)'.decode('utf-8'),
  '┗(＾0＾)┓'.decode('utf-8'),
  '໒( ͡ᵔ ͜ʖ ͡ᵔ )७'.decode('utf-8'),
  '(ノ°▽°)ノ︵┻━┻'.decode('utf-8'),
  'ᕕ╏ ͡ ▾ ͡ ╏┐'.decode('utf-8'),
  '¯\_( ͠° ͟ʖ °͠ )_/¯'.decode('utf-8'),
  '(ᓄಠ_ಠ)ᓄ'.decode('utf-8'),
  'ʕง•ᴥ•ʔง'.decode('utf-8'),
  '(ง’̀-‘́)ง'.decode('utf-8'),
  '(งಠ_ಠ)ง'.decode('utf-8'),
  '༼⁰o⁰；༽'.decode('utf-8'),
  'ԅ⁞ ◑ ₒ ◑ ⁞ᓄ'.decode('utf-8'),
  '། – _ – །'.decode('utf-8'),
  '༼つಠ益ಠ༽つ ─=≡ΣO))'.decode('utf-8'),
  'ヽ(⌐■_■)ノ♪♬'.decode('utf-8'),
  '♪ヽ( ⌒o⌒)人(⌒-⌒ )v ♪'.decode('utf-8'),
  '♪O<( ･ ∀ ･ )っ┌iii┐'.decode('utf-8'),
  '[ ⇀ ‿ ↼ ]'.decode('utf-8'),
  'ヽ(”`▽´)ﾉ'.decode('utf-8')]

def AddrFuncs(cmd, args, data, conn):
  chan = data['channel']
  if cmd.lower() == 'whohere':
    msg = "Users in %s: %s %s" % (chan, ' '.join(conn.nicks[chan]), str(len(conn.nicks[chan])))
    print msg
  elif cmd.lower() == 'lastmessages':
    for row in conn.lastMsg:
      print "%s: %s" % (row, conn.lastMsg[row])
  elif cmd.lower() == 'slap':
    target = args[0]
    slappee = data['sender'].split('!')[0]
    if target in conn.nicks:
      msg = "slaps %s with a floppy fish, then points at %s" % (target, slappee)
    else:
      msg = "can't find %s" % target
    conn.describe(msg, chan)
  elif cmd.lower() == 'part' and data['sender'] == trusted:
    chan = args[0]
    msg = ' '.join(args[1:])
    conn.leave(msg, chan)
  elif cmd.lower() == 'join' and data['sender'] == trusted:
    chan = args[0]
    conn.join(chan)
  elif cmd.lower() == 'act' and data['sender'] == trusted:
    chan = args[0]
    msg = ' '.join(args[1:])
    conn.describe(msg, chan)
  elif cmd.lower() == 'speak' and data['sender'] == trusted:
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
    if asker == trusted:
      conn.quit('goodbye for now')
    else:
      conn.say('┌∩┐(ಠ_ಠ)┌∩┐'.decode('utf-8'), chan)
  elif cmd.lower() == 'die':
    conn.say('nou', chan)

def UnAddrFuncs(cmd, args, data, conn):
  chan = data['channel']
  sendNick = data['sender'].split('!')[0]
  if cmd.lower() == '.cb' or cmd.lower() == '!cb':
    pass
  elif re.match('s/.+/.*/', cmd):
    pass # unobot is handling this function atm
    pre = cmd.split('/')[1]
    suf = cmd.split('/')[2]
    if conn.lastMsg[sendNick]:
      msgre = conn.lastMsg[sendNick].replace(pre, suf)
      msg = "%s meant to say: %s" % (sendNick, msgre)
      conn.say(msg, chan)
    else:
      conn.say('i fucked up', chan)
  elif cmd.lower() == '!help' or cmd.lower() == '.help':
    conn.say("happypizza doesn't want to help you", chan)
  elif cmd.lower() == 'happy':
    if args[0].lower() == 'birthday' or args[0].lower() == 'bday':
      conn.say('♪O<( ･ ∀ ･ )っ┌iii┐'.decode('utf-8'), chan)
  elif cmd.lower() == 'donger' or cmd.lower() == 'dong' or cmd.lower() == 'smoak':
    conn.say(random.choice(donger), chan)
  elif cmd.lower() == '!flip' or cmd.lower() == '.flip':
    conn.say('(ノ°▽°)ノ︵┻━┻'.decode('utf-8'), chan)
  elif cmd.lower() == '!unflip' or cmd.lower() == '.unflip':
    conn.say('┬─┬ノ(°▽°ノ)'.decode('utf-8'), chan)
  elif cmd.lower() == '^5':
    fiver = data['sender'].split('!')[0]
    chan = data['channel']
    msg = "high fives %s in the face" % fiver
    conn.describe(msg, chan)

def OnJoinFuncs(channel, conn):
  pass

def OtherJoinFuncs(data, conn):
  if data['nick'] == 'zeezey':
    conn.say('( ´・ω・)つ──☆✿✿✿✿✿✿ Welcome President zeezey!'.decode('utf-8'), data['channel'])
#  else:
#    conn.say('Hi my name is spacecake', data['channel'])

def OnKickedFuncs(msg, data, conn):
  pass

def OtherKickedFuncs(msg, data, conn):
  chan = data['channel']
  conn.say('╭∩╮ʕ•ᴥ•ʔ╭∩╮'.decode('utf-8'), chan)
