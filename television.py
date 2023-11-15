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
    if self.muted == False:
      self.muted = True
    elif self.muted == True:
      self.muted = False


  def channel_up(self):
    if self.channel == self.Max_CHANNEL:
      self.channel = self.MIN_CHANNEL
    else:
      self.channel = self.channel + 1

  def channel_down(self):
    if self.channel == self.MIN_CHANNEL:
      self.channel = self.MAX_CHANNEL
    else:
      self.channel = self.channel - 1

  def volume_up(self):
    if self.volume == self.MAX_VOLUME:
      self.volume = self.volume
    else:
      self.volume = self.volume + 1
  def volume_down(self):
    if self.volume == self.MAX_MIN:
      self.volume = self.volume
    else:
      self.volume = self.volume - 1
  def __str__(self):
    Power = self.status
    Channel = self.channel
    Volume = self.volume
