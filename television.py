class Television:
  
  self.MIN_VOLUME = 0
  self.MAX_VOLUME = 2
  self.MIN_CHANNEL = 0
  self.MAX_CHANNEL = 3

  def __init__(self):
    self.status = False
    self.muted = False
    self.volume = self.MIN_VOLUME
    self.channel = self.MIN_CHANNEL

  def power(self):
    if self.status == False:
      self.status = True
    elif self.status == True:
      self.status = False

  def mute(self):
    pass

  def channel_up(self):
    pass

  def channel_down(self):
    pass

  def volume_up(self):
    pass
  def volume_down(self):
    pass
  def __str__(self):
    Power = self.status
    Channel = self.channel
    Volume = self.volume
