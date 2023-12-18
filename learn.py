import random

class WordLearner:

  def __init__(self, word_list):
    self.word_list = word_list
    self.word_info = {}
    self.learned_words = []
    self.unlearned_words = []
    self.current_word = ''
    self.init_word_info()
    self.init_unlearned_words()
    self.random_word()

  def init_word_info(self):
    for word in self.word_list:
      info = {
        'explanation': self.generate_explanation(word),
        'example': self.generate_example(word),
        'synonym': self.generate_synonym(word),
        'antonym': self.generate_antonym(word),
        'root': self.generate_root(word),
        'affix': self.generate_affix(word),
        'choice_a': self.generate_choice_a(word),
        'choice_b': self.generate_choice_b(word),
        'choice_c': self.generate_choice_c(word),
        'choice_d': self.generate_choice_d(word),
      }
      self.word_info[word] = info

  def init_unlearned_words(self):
    self.unlearned_words = self.word_list[:]

  def random_word(self):
    if self.unlearned_words:
      word = random.choice(self.unlearned_words)
      self.current_word = word
      self.unlearned_words.remove(word)
      self.learned_words.append(word)
    else:
      self.current_word = ''

  def get_current_word(self):
    return self.current_word

  def get_current_word_info(self):
    if self.current_word:
      return self.word_info[self.current_word]
    else:
      return None

  def get_learned_words_count(self):
    return len(self.learned_words)

  def get_unlearned_words_count(self):
    return len(self.unlearned_words)

  def get_progress_percentage(self):
    if self.word_list:
      percentage = round(len(self.learned_words) / len(self.word_list) * 100, 2)
      return percentage
    else:
      return 0

  def next_word(self):
    self.random_word()

  def previous_word(self):
    if len(self.learned_words) > 1:
      self.current_word = self.learned_words[-1]
      self.learned_words.pop()
      self.unlearned_words.append(self.learned_words[-1])

  def generate_explanation(self, word):
    if word == 'apple':
      return 'a round fruit with red or green skin and a white inside'
    elif word == 'banana':
      return 'a long yellow fruit with a soft inside and a thick skin that you can peel off'
    elif word == 'cat':
      return 'a small animal with soft fur, a long tail, and sharp claws, that is often kept as a pet'
    elif word == 'dog':
      return 'a common animal with four legs, fur, and a tail, that is often kept as a pet or trained to work'
    elif word == 'elephant':
      return 'a very large gray animal with a long trunk and two long curved teeth'
    elif word == 'fish':
      return 'an animal that lives in water, has a tail and fins, and breathes with gills'
    elif word == 'giraffe':
      return 'a large African animal with a very long neck, long legs, and dark spots on its fur'
    elif word == 'house':
      return 'a building where people live, usually with one or more floors and a roof'
    elif word == 'ice':
      return 'water that has frozen and become solid'
    elif word == 'jacket':
      return 'a short coat that covers the upper part of the body'
    else:
      return 'unknown word'

  def generate_example(self, word):
    if word == 'apple':
      return 'She ate an apple for breakfast.'
    elif word == 'banana':
      return 'He peeled a banana and gave it to the monkey.'
    elif word == 'cat':
      return 'She has a black cat named Luna.'
    elif word == 'dog':
      return 'He walked his dog in the park.'
    elif word == 'elephant':
      return 'We saw an elephant at the zoo.'
    elif word == 'fish':
      return 'She likes to eat fish and chips.'
    elif word == 'giraffe':
      return 'The giraffe stretched its neck to reach the leaves.'
    elif word == 'house':
      return 'They live in a big house near the lake.'
    elif word == 'ice':
      return 'He put some ice in his drink.'
    elif word == 'jacket':
      return 'She wore a red jacket and a blue scarf.'
    else:
      return 'unknown word'

  def generate_synonym(self, word):
    if word == 'apple':
      return 'pome'
    elif word == 'banana':
      return 'plantain'
    elif word == 'cat':
      return 'feline'
    elif word == 'dog':
      return 'canine'
    elif word == 'elephant':
      return 'pachyderm'
    elif word == 'fish':
      return 'aquatic'
    elif word == 'giraffe':
      return 'camelopard'
    elif word == 'house':
      return 'dwelling'
    elif word == 'ice':
      return 'frost'
    elif word == 'jacket':
      return 'coat'
    else:
      return 'unknown word'

  def generate_antonym(self, word):
    if word == 'apple':
      return 'orange'
    elif word == 'banana':
      return 'grape'
    elif word == 'cat':
      return 'dog'
    elif word == 'dog':
      return 'cat'
    elif word == 'elephant':
      return 'mouse'
    elif word == 'fish':
      return 'bird'
    elif word == 'giraffe':
      return 'turtle'
    elif word == 'house':
      return 'tent'
    elif word == 'ice':
      return 'fire'
    elif word == 'jacket':
      return 'shirt'
    else:
      return 'unknown word'

  def generate_root(self, word):
    if word == 'apple':
      return 'ap'
    elif word == 'banana':
      return 'ban'
    elif word == 'cat':
      return 'cat'
    elif word == 'dog':
      return 'dog'
    elif word == 'elephant':
      return 'eleph'
    elif word == 'fish':
      return 'fish'
    elif word == 'giraffe':
      return 'giraff'
    elif word == 'house':
      return 'hous'
    elif word == 'ice':
      return 'ic'
    elif word == 'jacket':
      return 'jack'
    else:
      return 'unknown word'

  def generate_affix(self, word):
    if word == 'apple':
      return 'le'
    elif word == 'banana':
      return 'ana'
    elif word == 'cat':
      return ''
    elif word == 'dog':
      return ''
    elif word == 'elephant':
      return 'ant'
    elif word == 'fish':
      return ''
    elif word == 'giraffe':
      return 'e'
    elif word == 'house':
      return 'e'
    elif word == 'ice':
      return 'e'
    elif word == 'jacket':
      return 'et'
    else:
      return 'unknown word'

  def generate_choice_a(self, word):
    if word == 'apple':
      return 'pear'
    elif word == 'banana':
      return 'plantain'
    elif word == 'cat':
      return 'feline'
    elif word == 'dog':
      return 'canine'
    elif word == 'elephant':
      return 'pachyderm'
    elif word == 'fish':
      return 'aquatic'
    elif word == 'giraffe':
      return 'camelopard'
    elif word == 'house':
      return 'dwelling'
    elif word == 'ice':
      return 'frost'
    elif word == 'jacket':
      return 'coat'
    else:
      return 'unknown word'

  def generate_choice_b(self, word):
    if word == 'apple':
      return 'orange'
    elif word == 'banana':
      return 'grape'
    elif word == 'cat':
      return 'dog'
    elif word == 'dog':
      return 'cat'
    elif word == 'elephant':
      return 'mouse'
    elif word == 'fish':
      return 'bird'
    elif word == 'giraffe':
      return 'turtle'
    elif word == 'house':
      return 'tent'
    elif word == 'ice':
      return 'fire'
    elif word == 'jacket':
      return 'shirt'
    else:
      return 'unknown word'

  def generate_choice_c(self, word):
    if word == 'apple':
      return 'pome'
    elif word == 'banana':
      return 'berry'
    elif word == 'cat':
      return 'lion'
    elif word == 'dog':
      return 'wolf'
    elif word == 'elephant':
      return 'rhino'
    elif word == 'fish':
      return 'shark'
    elif word == 'giraffe':
      return 'zebra'
    elif word == 'house':
      return 'castle'
    elif word == 'ice':
      return 'snow'
    elif word == 'jacket':
      return 'sweater'
    else:
      return 'unknown word'

  def generate_choice_d(self, word):
    if word == 'apple':
      return 'lemon'
    elif word == 'banana':
      return 'melon'
    elif word == 'cat':
      return 'tiger'
    elif word == 'dog':
      return 'fox'
    elif word == 'elephant':
      return 'hippo'
    elif word == 'fish':
      return 'whale'
    elif word == 'giraffe':
      return 'horse'
    elif word == 'house':
      return 'cabin'
    elif word == 'ice':
      return 'water'
    elif word == 'jacket':
      return 'vest'
    else:
      return 'unknown word'

  def calculate_accuracy_and_compare(self, word, explanation, example, synonym, antonym, root, affix):
    # 初始化一个变量，用于存储正确的数量
    correct_count = 0
    # 初始化一个字典，用于存储对比结果
    compare = {}
    # 获取单词的真实信息
    word_info = self.word_info[word]
    # 比较解释是否正确
    if explanation == word_info['explanation']:
      correct_count += 1
      compare['explanation'] = True
    else:
      compare['explanation'] = False
    # 比较例句是否正确
    if example == word_info['example']:
      correct_count += 1
      compare['example'] = True
    else:
      compare['example'] = False
    # 比较同义词是否正确
    if synonym == word_info['synonym']:
      correct_count += 1
      compare['synonym'] = True
    else:
      compare['synonym'] = False
    # 比较反义词是否正确
    if antonym == word_info['antonym']:
      correct_count += 1
      compare['antonym'] = True
    else:
      compare['antonym'] = False
    # 比较词根是否正确
    if root == word_info['root']:
      correct_count += 1
      compare['root'] = True
    else:
      compare['root'] = False
    # 比较词缀是否正确
    if affix == word_info['affix']:
      correct_count += 1
      compare['affix'] = True
    else:
      compare['affix'] = False
    # 计算正确率，保留两位小数
    accuracy = round(correct_count / 6 * 100, 2)
    # 返回正确率和对比结果
    return accuracy, compare

  def calculate_accuracy_and_compare_quiz(self, word, choice_answer, blank_answer, judge_answer):
    # 初始化一个变量，用于存储正确的数量
    correct_count = 0
    # 初始化一个字典，用于存储对比结果
    compare = {}
    # 获取单词的真实信息
    word_info = self.word_info[word]
    # 比较选择题是否正确
    if choice_answer == 'C':
      correct_count += 1
      compare['choice'] = True
    else:
      compare['choice'] = False
    # 比较填空题是否正确
    if blank_answer == word_info['example']:
      correct_count += 1
      compare['blank'] = True
    else:
      compare['blank'] = False
    # 比较判断题是否正确
    if judge_answer == 'True':
      correct_count += 1
      compare['judge'] = True
    else:
      compare['judge'] = False
    # 计算正确率，保留两位小数
    accuracy = round(correct_count / 3 * 100, 2)
    # 返回正确率和对比结果
    return accuracy, compare

  def generate_quiz_questions(self, word):
    # 初始化一个变量，用于存储选择题
    choice_question = f'{word}的同义词是？'
    # 初始化一个列表，用于存储选择题的选项
    choice_options = [self.word_info[word]['choice_a'], self.word_info[word]['choice_b'], self.word_info[word]['choice_c'], self.word_info[word]['choice_d']]
    # 初始化一个变量，用于存储填空题
    blank_question = f'用{word}填空。'
    # 初始化一个变量，用于存储判断题
    judge_question = f'{word}的词根是{self.word_info[word]["root"]}（对或错）'
    # 返回选择题，填空题，判断题
    return choice_question, choice_options, blank_question, judge_question

  def answer_question(self, question):
    # 初始化一个变量，用于存储回答
    answer = ''
    # 如果问题是关于单词的解释
    if question.startswith('什么是'):
      # 获取问题中的单词
      word = question[3:]
      # 如果单词在单词列表中
      if word in self.word_list:
        # 获取单词的解释
        explanation = self.word_info[word]['explanation']
        # 将解释作为回答
        answer = explanation
      # 否则，回答不知道
      else:
        answer = '不知道'
    # 如果问题是关于单词的例句
    elif question.startswith('用'):
      # 获取问题中的单词
      word = question[1:-2]
      # 如果单词在单词列表中
      if word in self.word_list:
        # 获取单词的例句
        example = self.word_info[word]['example']
        # 将例句作为回答
        answer = example
      # 否则，回答不知道
      else:
        answer = '不知道'
    # 如果问题是关于单词的同义词
    elif question.startswith('什么和'):
      # 获取问题中的单词
      word = question[2:-2]
      # 如果单词在单词列表中
      if word in self.word_list:
        # 获取单词的同义词
        synonym = self.word_info[word]['synonym']
        # 将同义词作为回答
        answer = synonym
      # 否则，回答不知道
      else:
        answer = '不知道'
    # 如果问题是关于单词的反义词
    elif question.startswith('什么和'):
      # 获取问题中的单词
      word = question[2:-2]
      # 如果单词在单词列表中
      if word in self.word_list:
        # 获取单词的反义词
        antonym = self.word_info[word]['antonym']
        # 将反义词作为回答
        answer = antonym
      # 否则，回答不知道
      else:
        answer = '不知道'
    # 如果问题是关于单词的词根
    elif question.startswith('什么是'):
      # 获取问题中的单词
      word = question[3:-2]
      # 如果单词在单词列表中
      if word in self.word_list:
        # 获取单词的词根
        root = self.word_info[word]['root']
        # 将词根作为回答
        answer = root
      # 否则，回答不知道
      else:
        answer = '不知道'
    # 如果问题是关于单词的词缀
    elif question.startswith('什么是'):
      # 获取问题中的单词
      word = question[3:-2]
      # 如果单词在单词列表中
      if word in self.word_list:
        # 获取单词的词缀
        affix = self.word_info[word]['affix']
        # 将词缀作为回答
        answer = affix
      # 否则，回答不知道
      else:
        answer = '不知道'
    # 如果问题是其他的
    else:
      # 回答不懂
      answer = '不懂'
    # 返回回答
    return answer
  def generate_blank_question(self, word):
    if word == 'apple':
      return 'She ate an ______ for breakfast.'
    elif word == 'banana':
      return 'He peeled a ______ and gave it to the monkey.'
    elif word == 'cat':
      return 'She has a black ______ named Luna.'
    elif word == 'dog':
      return 'He walked his ______ in the park.'
    elif word == 'elephant':
      return 'We saw an ______ at the zoo.'
    elif word == 'fish':
      return 'She likes to eat ______ and chips.'
    elif word == 'giraffe':
      return 'The ______ stretched its neck to reach the leaves.'
    elif word == 'house':
      return 'They live in a big ______ near the lake.'
    elif word == 'ice':
      return 'He put some ______ in his drink.'
    elif word == 'jacket':
      return 'She wore a red ______ and a blue scarf.'
    else:
      return 'unknown word'
  def generate_judge_question(self, word):
    if word == 'apple':
      return 'apple的词根是ap（对或错）'
    elif word == 'banana':
      return 'banana的词缀是ana（对或错）'
    elif word == 'cat':
      return 'cat的反义词是dog（对或错）'
    elif word == 'dog':
      return 'dog的同义词是canine（对或错）'
    elif word == 'elephant':
      return 'elephant的词根是eleph（对或错）'
    elif word == 'fish':
      return 'fish的词缀是ish（对或错）'
    elif word == 'giraffe':
      return 'giraffe的同义词是camelopard（对或错）'
    elif word == 'house':
      return 'house的反义词是tent（对或错）'
    elif word == 'ice':
      return 'ice的词根是ic（对或错）'
    elif word == 'jacket':
      return 'jacket的词缀是et（对或错）'
    else:
      return 'unknown word'