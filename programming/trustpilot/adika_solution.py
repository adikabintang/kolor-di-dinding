import telebot
import sys
import logging
# https://followthewhiterabbit.trustpilot.com/cs/step3.html

logging.basicConfig(filename="tb.log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

logger = logging.getLogger('tb')
logger.setLevel(logging.DEBUG)

logger.debug("ooooi")

class Solution:
    def __init__(self):
        self.running = False
    
    def solve(self, bot, message):
        self.running = True
        anagram_ori = "poultry outwits ants"
        # ana_arr = anagram_ori.split()
        # print(ana_arr)

        wordlist = open('wordlist', 'r')
        words = wordlist.readlines()
        usable_words = []
        for word in words:
            # print(word.strip())
            if self.__is_permutation(anagram_ori, word.strip()):
                usable_words.append(word.strip())

        wordlist.close()

        #usable_words = usable_words[:3]
        result_file = open("result.txt", "a")
        # make a permutation of all usable words
        for i in range(len(usable_words)):
            for j in range(len(usable_words)):
                for k in range(len(usable_words)):
                    if i != j and i != k and j != k:
                        # print("%s %s %s" % (usable_words[i], usable_words[j], usable_words[k][k]))
                        s = usable_words[i] + " " + usable_words[j] + " " + usable_words[k]
                        if self.__is_fully_anagram(s, anagram_ori):
                            hash_hex = hashlib.md5(s.encode('utf-8')).hexdigest()
                            if hash_hex == "e4820b45d2277f3844eac66c903e84be" or \
                                hash_hex == "23170acc097c24edb98fc5488ab033fe" or \
                                hash_hex == "665e5bcb0c20062fe8abaaf4628bb154":

                                print(s)
                                result_file.write(s + "\n")
                                logger.info(s)
                                # send to telegram
                                bot.send_message(message.chat.id, s)

        result_file.close()
        print("finished!")
        logger.debug("computation finished")
        bot.send_message(message.chat.id, "computation finished!")

    def __is_permutation(self, s1: str, s2: str):
        all_char = [0] * 256
        for i in range(len(s1)):
            all_char[ord(s1[i])] += 1
        
        for i in range(len(s2)):
            index = ord(s2[i])
            all_char[index] -= 1
            if all_char[index] < 0:
                return False
        
        return True
    
    def __is_fully_anagram(self, s1: str, s2: str):
        if len(s1) != len(s2):
            return False
        else:
            return self.__is_permutation(s1, s2)

if sys.argv[1]:
    token = sys.argv[1]
    print(token)
else:
    print("enter telegram token")
    exit()

solution = Solution()
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    solution.solve(bot, message)

bot.polling()
