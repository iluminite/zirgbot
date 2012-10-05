import os
import sys
from twisted.internet import reactor, protocol
from twisted.words.protocols import irc

from irclogger.models import Log

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class LoggingIRCClient(irc.IRCClient):
    logfile = file('/tmp/msg.txt', 'a+')

    nickname = 'omsbot'

    def signedOn(self):
        self.join('#oms')

    def privmsg(self, user, channel, message):
        self.logfile.write(user.split('!')[0] + ' -> ' + message + '\n')
        self.logfile.flush()
        # XXX - hardcoded channel for time being
        l = Log(user=user.split('!')[0], msg=message, channel='1')
        l.save()

def main():
    f = protocol.ReconnectingClientFactory()
    f.protocol = LoggingIRCClient
    reactor.connectTCP('irc.freenode.net', 6667, f)
    reactor.run()

if __name__ == '__main__':
    main()

