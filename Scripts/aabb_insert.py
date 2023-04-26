import matplotlib.pyplot as plt

def test():
    print( "test" )

def plot():
    sizes = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,
              190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,
              360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,
              530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,
              700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,
              870,880,890,900,910,920,930,940,950,960,970,980,990,1000]

    depths = [0,8,12,19,25,30,36,39,41,43,45,48,50,53,55,58,59,59,59,59,60,61,61,64,
              66,67,67,67,67,67,68,68,69,70,70,70,70,70,70,73,73,74,74,75,75,75,75,
              75,76,76,76,76,76,76,77,77,78,79,80,80,82,82,82,82,82,82,83,83,83,83,
              83,83,84,84,84,84,84,84,85,86,86,87,87,87,87,88,88,88,88,88,88,88,89,
              89,89,89,90,91,92,92,93]

    plt.plot(sizes, depths)
    plt.ylabel('Depth')
    plt.xlabel('Number of objects')
    plt.show()
