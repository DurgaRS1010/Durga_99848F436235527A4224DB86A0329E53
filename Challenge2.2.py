"""creating a class called player.The class should have a method play() which prints "The player is playing cricket". Derive 2 classes, Batsman & bowler from player class.override the play() method in each derived class to print "the batsman is batting" and "the bowleris bowling".creating objects for Batsman & bowler classes and call the play() method for each object."""

class player:

  def play(self):
      print("The player is playing cricket.")

class Batsman(player):
  def play(self):
    print("The batsman is batting.")

class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

batsman = Batsman ()
bowler = Bowler ()

batsman.play()
bowler.play()