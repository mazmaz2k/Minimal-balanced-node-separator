input = """
% Instantiation generated by
% DLV [build BEN/Oct 14 2010   gcc 4.4.3]

% EDB facts:
controlled_by(1,2,12,4,4).
controlled_by(1,3,12,14,10).
controlled_by(1,4,5,4,11).
controlled_by(1,5,11,6,8).
controlled_by(1,6,3,4,6).
controlled_by(1,8,5,11,12).
controlled_by(1,9,7,7,3).
controlled_by(1,12,11,6,8).
controlled_by(1,12,15,11,7).
controlled_by(1,12,15,14,4).
controlled_by(1,13,4,15,14).
controlled_by(1,15,10,2,3).
controlled_by(2,5,14,11,5).
controlled_by(2,6,3,4,8).
controlled_by(2,6,3,15,13).
controlled_by(2,7,9,10,11).
controlled_by(2,7,12,3,7).
controlled_by(2,11,4,14,7).
controlled_by(2,11,12,13,7).
controlled_by(2,12,1,4,7).
controlled_by(2,12,1,5,4).
controlled_by(2,12,8,1,10).
controlled_by(2,14,1,7,8).
controlled_by(2,14,3,5,4).
controlled_by(3,1,1,5,7).
controlled_by(3,2,10,15,9).
controlled_by(3,4,5,15,14).
controlled_by(3,5,15,6,8).
controlled_by(3,6,7,4,12).
controlled_by(3,7,8,7,13).
controlled_by(3,7,15,7,12).
controlled_by(3,9,10,4,8).
controlled_by(3,11,13,6,4).
controlled_by(3,13,14,6,12).
controlled_by(3,14,2,1,5).
controlled_by(3,14,2,8,12).
controlled_by(4,1,5,11,12).
controlled_by(4,2,8,6,3).
controlled_by(4,5,11,10,15).
controlled_by(4,7,11,13,2).
controlled_by(4,8,10,5,3).
controlled_by(4,9,1,5,3).
controlled_by(4,10,12,7,14).
controlled_by(4,11,1,8,3).
controlled_by(4,11,14,7,14).
controlled_by(4,12,10,5,6).
controlled_by(4,13,9,14,11).
controlled_by(4,15,13,9,9).
controlled_by(5,1,6,13,9).
controlled_by(5,1,14,4,10).
controlled_by(5,2,8,6,6).
controlled_by(5,3,13,3,4).
controlled_by(5,4,6,15,2).
controlled_by(5,7,15,2,8).
controlled_by(5,11,3,6,9).
controlled_by(5,11,7,6,6).
controlled_by(5,12,8,13,15).
controlled_by(5,13,2,6,11).
controlled_by(5,15,9,13,6).
controlled_by(5,15,15,4,1).
controlled_by(6,2,14,12,8).
controlled_by(6,3,9,15,4).
controlled_by(6,3,13,11,12).
controlled_by(6,5,2,1,1).
controlled_by(6,5,9,2,5).
controlled_by(6,9,2,12,15).
controlled_by(6,9,9,2,2).
controlled_by(6,9,10,7,7).
controlled_by(6,10,7,10,15).
controlled_by(6,13,5,14,13).
controlled_by(6,14,3,14,12).
controlled_by(6,15,11,5,5).
controlled_by(7,3,6,15,5).
controlled_by(7,5,3,4,10).
controlled_by(7,5,6,2,12).
controlled_by(7,5,12,5,4).
controlled_by(7,11,3,4,4).
controlled_by(7,11,4,1,10).
controlled_by(7,12,14,9,8).
controlled_by(7,13,12,14,9).
controlled_by(7,14,5,2,1).
controlled_by(7,15,4,12,2).
controlled_by(7,15,10,8,6).
controlled_by(7,15,13,1,8).
controlled_by(8,5,10,1,6).
controlled_by(8,5,10,12,1).
controlled_by(8,7,10,1,2).
controlled_by(8,7,10,5,14).
controlled_by(8,9,11,13,5).
controlled_by(8,9,12,6,3).
controlled_by(8,13,1,2,6).
controlled_by(8,14,3,3,4).
controlled_by(8,14,6,5,15).
controlled_by(8,14,9,1,14).
controlled_by(8,14,11,4,10).
controlled_by(8,15,12,11,6).
controlled_by(9,4,10,11,13).
controlled_by(9,5,10,15,3).
controlled_by(9,6,7,5,13).
controlled_by(9,8,6,10,6).
controlled_by(9,10,4,2,5).
controlled_by(9,10,8,6,14).
controlled_by(9,11,6,3,1).
controlled_by(9,12,10,11,8).
controlled_by(9,14,2,1,4).
controlled_by(9,15,1,15,7).
controlled_by(9,15,2,11,10).
controlled_by(9,15,11,11,11).
controlled_by(10,1,15,9,11).
controlled_by(10,4,1,1,8).
controlled_by(10,6,1,11,3).
controlled_by(10,6,4,1,11).
controlled_by(10,6,14,1,6).
controlled_by(10,7,4,8,6).
controlled_by(10,9,3,11,11).
controlled_by(10,9,9,4,2).
controlled_by(10,13,15,12,15).
controlled_by(10,14,2,2,4).
controlled_by(10,14,4,6,7).
controlled_by(10,15,11,12,13).
controlled_by(11,1,6,7,4).
controlled_by(11,2,9,10,2).
controlled_by(11,3,14,5,7).
controlled_by(11,3,15,13,9).
controlled_by(11,4,4,14,1).
controlled_by(11,4,6,14,4).
controlled_by(11,10,5,4,7).
controlled_by(11,10,12,10,9).
controlled_by(11,12,9,3,12).
controlled_by(11,12,12,9,3).
controlled_by(11,13,7,3,1).
controlled_by(11,14,8,6,7).
controlled_by(12,1,4,6,1).
controlled_by(12,3,6,9,9).
controlled_by(12,3,13,14,6).
controlled_by(12,3,14,4,1).
controlled_by(12,6,1,2,1).
controlled_by(12,7,5,15,11).
controlled_by(12,7,6,3,7).
controlled_by(12,7,7,15,2).
controlled_by(12,8,9,11,3).
controlled_by(12,10,13,2,10).
controlled_by(12,11,1,3,11).
controlled_by(12,14,3,13,15).
controlled_by(13,2,4,14,10).
controlled_by(13,2,11,10,15).
controlled_by(13,3,3,3,3).
controlled_by(13,3,15,7,9).
controlled_by(13,5,1,8,6).
controlled_by(13,5,9,7,5).
controlled_by(13,7,3,11,2).
controlled_by(13,9,6,6,9).
controlled_by(13,9,8,7,12).
controlled_by(13,12,5,12,4).
controlled_by(13,14,3,3,11).
controlled_by(13,14,3,15,8).
controlled_by(14,1,5,7,12).
controlled_by(14,1,7,7,4).
controlled_by(14,1,8,8,4).
controlled_by(14,4,5,5,9).
controlled_by(14,5,6,9,11).
controlled_by(14,6,5,2,11).
controlled_by(14,6,11,3,12).
controlled_by(14,7,1,3,10).
controlled_by(14,7,5,1,9).
controlled_by(14,9,12,3,4).
controlled_by(14,11,1,4,5).
controlled_by(14,13,4,3,15).
controlled_by(15,1,9,11,6).
controlled_by(15,3,5,13,5).
controlled_by(15,4,1,7,4).
controlled_by(15,5,2,9,10).
controlled_by(15,5,4,12,6).
controlled_by(15,5,11,4,13).
controlled_by(15,6,13,13,5).
controlled_by(15,6,13,14,9).
controlled_by(15,6,14,7,14).
controlled_by(15,8,10,9,6).
controlled_by(15,12,3,12,9).
controlled_by(15,12,8,10,5).
produced_by(p1,11,5,3,1).
produced_by(p2,3,9,6,14).
produced_by(p3,5,9,3,14).
produced_by(p4,5,15,14,10).
produced_by(p5,4,14,8,14).
produced_by(p6,5,5,13,14).
produced_by(p7,11,3,5,8).
produced_by(p8,12,1,8,7).
produced_by(p9,5,10,14,15).
produced_by(p10,11,11,5,7).
produced_by(p11,11,8,5,15).
produced_by(p12,14,10,1,9).
produced_by(p13,15,9,14,11).
produced_by(p14,5,12,1,15).
produced_by(p15,6,6,14,9).
produced_by(p16,6,6,7,3).
produced_by(p17,1,5,9,3).
produced_by(p18,7,13,9,2).
produced_by(p19,12,5,8,3).
produced_by(p20,7,9,11,13).
produced_by(p21,9,10,9,13).
produced_by(p22,13,9,12,3).
produced_by(p23,6,11,11,12).
produced_by(p24,1,2,6,8).
produced_by(p25,13,6,10,11).
produced_by(p26,3,10,12,7).
produced_by(p27,15,11,9,6).
produced_by(p28,4,11,10,12).
produced_by(p29,12,3,1,9).
produced_by(p30,4,13,3,9).
produced_by(p31,15,5,12,7).
produced_by(p32,13,9,15,2).
produced_by(p33,14,1,12,9).
produced_by(p34,11,15,15,10).
produced_by(p35,11,15,7,6).
produced_by(p36,10,1,3,7).
produced_by(p37,11,3,7,14).
produced_by(p38,7,10,14,6).
produced_by(p39,14,11,13,4).
produced_by(p40,4,4,5,3).
produced_by(p41,4,2,11,14).
produced_by(p42,1,2,15,11).
produced_by(p43,8,13,2,2).
produced_by(p44,6,11,15,1).
produced_by(p45,5,14,6,4).
produced_by(p46,8,4,1,13).
produced_by(p47,14,13,1,3).
produced_by(p48,8,13,12,4).
produced_by(p49,14,14,2,14).
produced_by(p50,15,9,2,7).
produced_by(p51,13,10,15,3).
produced_by(p52,12,7,3,1).
produced_by(p53,5,8,11,4).
produced_by(p54,4,12,8,2).
produced_by(p55,1,1,11,9).
produced_by(p56,13,7,12,3).
produced_by(p57,12,5,8,3).
produced_by(p58,5,9,9,3).
produced_by(p59,10,1,5,6).
produced_by(p60,14,15,14,10).
produced_by(p61,14,9,5,2).
produced_by(p62,5,12,11,6).
produced_by(p63,4,6,6,8).
produced_by(p64,5,2,10,1).
produced_by(p65,13,3,4,3).
produced_by(p66,3,4,12,5).
produced_by(p67,11,1,10,9).
produced_by(p68,7,15,3,6).
produced_by(p69,9,7,14,5).
produced_by(p70,11,9,10,14).
produced_by(p71,15,7,14,11).
produced_by(p72,15,8,3,13).
produced_by(p73,2,6,7,5).
produced_by(p74,2,3,9,4).
produced_by(p75,10,10,13,2).
produced_by(p76,10,7,14,10).
produced_by(p77,6,4,14,8).
produced_by(p78,13,9,13,4).
produced_by(p79,15,11,14,15).
produced_by(p80,4,8,4,5).
produced_by(p81,6,10,1,7).
produced_by(p82,12,1,10,13).
produced_by(p83,3,14,14,12).
produced_by(p84,13,4,6,10).
produced_by(p85,8,4,2,5).
produced_by(p86,4,14,15,11).
produced_by(p87,2,5,2,12).
produced_by(p88,12,12,8,2).
produced_by(p89,6,9,15,9).
produced_by(p90,1,2,6,3).
produced_by(p91,15,12,6,4).
produced_by(p92,15,3,13,7).
produced_by(p93,14,14,3,2).
produced_by(p94,5,2,4,6).
produced_by(p95,13,12,2,10).
produced_by(p96,8,9,3,13).
produced_by(p97,9,3,13,2).
produced_by(p98,4,11,4,10).
produced_by(p99,7,2,14,6).
produced_by(p100,4,11,5,2).
produced_by(p101,2,7,11,13).
produced_by(p102,1,14,10,5).
produced_by(p103,11,11,14,10).
produced_by(p104,11,9,15,12).
produced_by(p105,11,12,13,6).
produced_by(p106,7,8,15,13).
produced_by(p107,1,5,11,5).
produced_by(p108,1,15,13,9).
produced_by(p109,13,8,6,5).
produced_by(p110,14,15,10,1).
produced_by(p111,2,15,10,4).
produced_by(p112,8,9,7,10).
produced_by(p113,13,11,7,4).
produced_by(p114,4,7,9,4).
produced_by(p115,3,11,15,3).
produced_by(p116,10,13,3,14).
produced_by(p117,12,8,11,2).
produced_by(p118,14,5,9,7).
produced_by(p119,11,4,11,11).
produced_by(p120,4,2,12,8).
produced_by(p121,13,4,12,8).
produced_by(p122,2,12,3,4).
produced_by(p123,7,10,14,8).
produced_by(p124,14,1,13,2).
produced_by(p125,1,8,4,14).
produced_by(p126,12,12,6,15).
produced_by(p127,7,8,10,3).
produced_by(p128,1,13,10,5).
produced_by(p129,1,13,4,2).
produced_by(p130,1,14,13,14).
produced_by(p131,8,11,6,6).
produced_by(p132,3,4,7,3).
produced_by(p133,11,2,9,15).
produced_by(p134,6,6,14,12).
produced_by(p135,5,15,6,12).
produced_by(p136,12,8,2,5).
produced_by(p137,12,12,13,13).
produced_by(p138,10,10,11,2).
produced_by(p139,12,9,7,7).
produced_by(p140,12,6,1,14).
produced_by(p141,7,9,13,12).
produced_by(p142,6,3,1,2).
produced_by(p143,9,13,14,13).
produced_by(p144,5,7,2,2).
produced_by(p145,3,14,14,13).
produced_by(p146,1,1,14,4).
produced_by(p147,9,13,10,5).
produced_by(p148,10,11,11,8).
produced_by(p149,11,15,5,2).
produced_by(p150,10,12,10,3).
produced_by(p151,9,8,7,14).
produced_by(p152,14,8,7,2).
produced_by(p153,14,12,6,14).
produced_by(p154,12,4,2,6).
produced_by(p155,8,4,2,2).
produced_by(p156,14,4,10,9).
produced_by(p157,4,6,2,13).
produced_by(p158,9,12,7,2).
produced_by(p159,11,14,7,10).
produced_by(p160,6,5,3,11).
produced_by(p161,1,8,9,13).
produced_by(p162,3,3,10,3).
produced_by(p163,6,3,4,11).
produced_by(p164,7,5,4,10).
produced_by(p165,2,13,14,10).
produced_by(p166,1,5,12,11).
produced_by(p167,3,10,12,1).
produced_by(p168,15,14,11,15).
produced_by(p169,13,12,4,8).
produced_by(p170,6,13,10,11).
produced_by(p171,8,5,6,14).
produced_by(p172,10,1,15,11).
produced_by(p173,13,5,6,13).
produced_by(p174,9,9,1,4).
produced_by(p175,3,12,4,2).
produced_by(p176,3,6,9,7).
produced_by(p177,2,12,14,7).
produced_by(p178,2,8,9,1).
produced_by(p179,13,6,6,14).
produced_by(p180,7,5,1,11).



"""

output = """
{controlled_by(1,12,11,6,8), controlled_by(1,12,15,11,7), controlled_by(1,12,15,14,4), controlled_by(1,13,4,15,14), controlled_by(1,15,10,2,3), controlled_by(1,2,12,4,4), controlled_by(1,3,12,14,10), controlled_by(1,4,5,4,11), controlled_by(1,5,11,6,8), controlled_by(1,6,3,4,6), controlled_by(1,8,5,11,12), controlled_by(1,9,7,7,3), controlled_by(10,1,15,9,11), controlled_by(10,13,15,12,15), controlled_by(10,14,2,2,4), controlled_by(10,14,4,6,7), controlled_by(10,15,11,12,13), controlled_by(10,4,1,1,8), controlled_by(10,6,1,11,3), controlled_by(10,6,14,1,6), controlled_by(10,6,4,1,11), controlled_by(10,7,4,8,6), controlled_by(10,9,3,11,11), controlled_by(10,9,9,4,2), controlled_by(11,1,6,7,4), controlled_by(11,10,12,10,9), controlled_by(11,10,5,4,7), controlled_by(11,12,12,9,3), controlled_by(11,12,9,3,12), controlled_by(11,13,7,3,1), controlled_by(11,14,8,6,7), controlled_by(11,2,9,10,2), controlled_by(11,3,14,5,7), controlled_by(11,3,15,13,9), controlled_by(11,4,4,14,1), controlled_by(11,4,6,14,4), controlled_by(12,1,4,6,1), controlled_by(12,10,13,2,10), controlled_by(12,11,1,3,11), controlled_by(12,14,3,13,15), controlled_by(12,3,13,14,6), controlled_by(12,3,14,4,1), controlled_by(12,3,6,9,9), controlled_by(12,6,1,2,1), controlled_by(12,7,5,15,11), controlled_by(12,7,6,3,7), controlled_by(12,7,7,15,2), controlled_by(12,8,9,11,3), controlled_by(13,12,5,12,4), controlled_by(13,14,3,15,8), controlled_by(13,14,3,3,11), controlled_by(13,2,11,10,15), controlled_by(13,2,4,14,10), controlled_by(13,3,15,7,9), controlled_by(13,3,3,3,3), controlled_by(13,5,1,8,6), controlled_by(13,5,9,7,5), controlled_by(13,7,3,11,2), controlled_by(13,9,6,6,9), controlled_by(13,9,8,7,12), controlled_by(14,1,5,7,12), controlled_by(14,1,7,7,4), controlled_by(14,1,8,8,4), controlled_by(14,11,1,4,5), controlled_by(14,13,4,3,15), controlled_by(14,4,5,5,9), controlled_by(14,5,6,9,11), controlled_by(14,6,11,3,12), controlled_by(14,6,5,2,11), controlled_by(14,7,1,3,10), controlled_by(14,7,5,1,9), controlled_by(14,9,12,3,4), controlled_by(15,1,9,11,6), controlled_by(15,12,3,12,9), controlled_by(15,12,8,10,5), controlled_by(15,3,5,13,5), controlled_by(15,4,1,7,4), controlled_by(15,5,11,4,13), controlled_by(15,5,2,9,10), controlled_by(15,5,4,12,6), controlled_by(15,6,13,13,5), controlled_by(15,6,13,14,9), controlled_by(15,6,14,7,14), controlled_by(15,8,10,9,6), controlled_by(2,11,12,13,7), controlled_by(2,11,4,14,7), controlled_by(2,12,1,4,7), controlled_by(2,12,1,5,4), controlled_by(2,12,8,1,10), controlled_by(2,14,1,7,8), controlled_by(2,14,3,5,4), controlled_by(2,5,14,11,5), controlled_by(2,6,3,15,13), controlled_by(2,6,3,4,8), controlled_by(2,7,12,3,7), controlled_by(2,7,9,10,11), controlled_by(3,1,1,5,7), controlled_by(3,11,13,6,4), controlled_by(3,13,14,6,12), controlled_by(3,14,2,1,5), controlled_by(3,14,2,8,12), controlled_by(3,2,10,15,9), controlled_by(3,4,5,15,14), controlled_by(3,5,15,6,8), controlled_by(3,6,7,4,12), controlled_by(3,7,15,7,12), controlled_by(3,7,8,7,13), controlled_by(3,9,10,4,8), controlled_by(4,1,5,11,12), controlled_by(4,10,12,7,14), controlled_by(4,11,1,8,3), controlled_by(4,11,14,7,14), controlled_by(4,12,10,5,6), controlled_by(4,13,9,14,11), controlled_by(4,15,13,9,9), controlled_by(4,2,8,6,3), controlled_by(4,5,11,10,15), controlled_by(4,7,11,13,2), controlled_by(4,8,10,5,3), controlled_by(4,9,1,5,3), controlled_by(5,1,14,4,10), controlled_by(5,1,6,13,9), controlled_by(5,11,3,6,9), controlled_by(5,11,7,6,6), controlled_by(5,12,8,13,15), controlled_by(5,13,2,6,11), controlled_by(5,15,15,4,1), controlled_by(5,15,9,13,6), controlled_by(5,2,8,6,6), controlled_by(5,3,13,3,4), controlled_by(5,4,6,15,2), controlled_by(5,7,15,2,8), controlled_by(6,10,7,10,15), controlled_by(6,13,5,14,13), controlled_by(6,14,3,14,12), controlled_by(6,15,11,5,5), controlled_by(6,2,14,12,8), controlled_by(6,3,13,11,12), controlled_by(6,3,9,15,4), controlled_by(6,5,2,1,1), controlled_by(6,5,9,2,5), controlled_by(6,9,10,7,7), controlled_by(6,9,2,12,15), controlled_by(6,9,9,2,2), controlled_by(7,11,3,4,4), controlled_by(7,11,4,1,10), controlled_by(7,12,14,9,8), controlled_by(7,13,12,14,9), controlled_by(7,14,5,2,1), controlled_by(7,15,10,8,6), controlled_by(7,15,13,1,8), controlled_by(7,15,4,12,2), controlled_by(7,3,6,15,5), controlled_by(7,5,12,5,4), controlled_by(7,5,3,4,10), controlled_by(7,5,6,2,12), controlled_by(8,13,1,2,6), controlled_by(8,14,11,4,10), controlled_by(8,14,3,3,4), controlled_by(8,14,6,5,15), controlled_by(8,14,9,1,14), controlled_by(8,15,12,11,6), controlled_by(8,5,10,1,6), controlled_by(8,5,10,12,1), controlled_by(8,7,10,1,2), controlled_by(8,7,10,5,14), controlled_by(8,9,11,13,5), controlled_by(8,9,12,6,3), controlled_by(9,10,4,2,5), controlled_by(9,10,8,6,14), controlled_by(9,11,6,3,1), controlled_by(9,12,10,11,8), controlled_by(9,14,2,1,4), controlled_by(9,15,1,15,7), controlled_by(9,15,11,11,11), controlled_by(9,15,2,11,10), controlled_by(9,4,10,11,13), controlled_by(9,5,10,15,3), controlled_by(9,6,7,5,13), controlled_by(9,8,6,10,6), produced_by(p1,11,5,3,1), produced_by(p10,11,11,5,7), produced_by(p100,4,11,5,2), produced_by(p101,2,7,11,13), produced_by(p102,1,14,10,5), produced_by(p103,11,11,14,10), produced_by(p104,11,9,15,12), produced_by(p105,11,12,13,6), produced_by(p106,7,8,15,13), produced_by(p107,1,5,11,5), produced_by(p108,1,15,13,9), produced_by(p109,13,8,6,5), produced_by(p11,11,8,5,15), produced_by(p110,14,15,10,1), produced_by(p111,2,15,10,4), produced_by(p112,8,9,7,10), produced_by(p113,13,11,7,4), produced_by(p114,4,7,9,4), produced_by(p115,3,11,15,3), produced_by(p116,10,13,3,14), produced_by(p117,12,8,11,2), produced_by(p118,14,5,9,7), produced_by(p119,11,4,11,11), produced_by(p12,14,10,1,9), produced_by(p120,4,2,12,8), produced_by(p121,13,4,12,8), produced_by(p122,2,12,3,4), produced_by(p123,7,10,14,8), produced_by(p124,14,1,13,2), produced_by(p125,1,8,4,14), produced_by(p126,12,12,6,15), produced_by(p127,7,8,10,3), produced_by(p128,1,13,10,5), produced_by(p129,1,13,4,2), produced_by(p13,15,9,14,11), produced_by(p130,1,14,13,14), produced_by(p131,8,11,6,6), produced_by(p132,3,4,7,3), produced_by(p133,11,2,9,15), produced_by(p134,6,6,14,12), produced_by(p135,5,15,6,12), produced_by(p136,12,8,2,5), produced_by(p137,12,12,13,13), produced_by(p138,10,10,11,2), produced_by(p139,12,9,7,7), produced_by(p14,5,12,1,15), produced_by(p140,12,6,1,14), produced_by(p141,7,9,13,12), produced_by(p142,6,3,1,2), produced_by(p143,9,13,14,13), produced_by(p144,5,7,2,2), produced_by(p145,3,14,14,13), produced_by(p146,1,1,14,4), produced_by(p147,9,13,10,5), produced_by(p148,10,11,11,8), produced_by(p149,11,15,5,2), produced_by(p15,6,6,14,9), produced_by(p150,10,12,10,3), produced_by(p151,9,8,7,14), produced_by(p152,14,8,7,2), produced_by(p153,14,12,6,14), produced_by(p154,12,4,2,6), produced_by(p155,8,4,2,2), produced_by(p156,14,4,10,9), produced_by(p157,4,6,2,13), produced_by(p158,9,12,7,2), produced_by(p159,11,14,7,10), produced_by(p16,6,6,7,3), produced_by(p160,6,5,3,11), produced_by(p161,1,8,9,13), produced_by(p162,3,3,10,3), produced_by(p163,6,3,4,11), produced_by(p164,7,5,4,10), produced_by(p165,2,13,14,10), produced_by(p166,1,5,12,11), produced_by(p167,3,10,12,1), produced_by(p168,15,14,11,15), produced_by(p169,13,12,4,8), produced_by(p17,1,5,9,3), produced_by(p170,6,13,10,11), produced_by(p171,8,5,6,14), produced_by(p172,10,1,15,11), produced_by(p173,13,5,6,13), produced_by(p174,9,9,1,4), produced_by(p175,3,12,4,2), produced_by(p176,3,6,9,7), produced_by(p177,2,12,14,7), produced_by(p178,2,8,9,1), produced_by(p179,13,6,6,14), produced_by(p18,7,13,9,2), produced_by(p180,7,5,1,11), produced_by(p19,12,5,8,3), produced_by(p2,3,9,6,14), produced_by(p20,7,9,11,13), produced_by(p21,9,10,9,13), produced_by(p22,13,9,12,3), produced_by(p23,6,11,11,12), produced_by(p24,1,2,6,8), produced_by(p25,13,6,10,11), produced_by(p26,3,10,12,7), produced_by(p27,15,11,9,6), produced_by(p28,4,11,10,12), produced_by(p29,12,3,1,9), produced_by(p3,5,9,3,14), produced_by(p30,4,13,3,9), produced_by(p31,15,5,12,7), produced_by(p32,13,9,15,2), produced_by(p33,14,1,12,9), produced_by(p34,11,15,15,10), produced_by(p35,11,15,7,6), produced_by(p36,10,1,3,7), produced_by(p37,11,3,7,14), produced_by(p38,7,10,14,6), produced_by(p39,14,11,13,4), produced_by(p4,5,15,14,10), produced_by(p40,4,4,5,3), produced_by(p41,4,2,11,14), produced_by(p42,1,2,15,11), produced_by(p43,8,13,2,2), produced_by(p44,6,11,15,1), produced_by(p45,5,14,6,4), produced_by(p46,8,4,1,13), produced_by(p47,14,13,1,3), produced_by(p48,8,13,12,4), produced_by(p49,14,14,2,14), produced_by(p5,4,14,8,14), produced_by(p50,15,9,2,7), produced_by(p51,13,10,15,3), produced_by(p52,12,7,3,1), produced_by(p53,5,8,11,4), produced_by(p54,4,12,8,2), produced_by(p55,1,1,11,9), produced_by(p56,13,7,12,3), produced_by(p57,12,5,8,3), produced_by(p58,5,9,9,3), produced_by(p59,10,1,5,6), produced_by(p6,5,5,13,14), produced_by(p60,14,15,14,10), produced_by(p61,14,9,5,2), produced_by(p62,5,12,11,6), produced_by(p63,4,6,6,8), produced_by(p64,5,2,10,1), produced_by(p65,13,3,4,3), produced_by(p66,3,4,12,5), produced_by(p67,11,1,10,9), produced_by(p68,7,15,3,6), produced_by(p69,9,7,14,5), produced_by(p7,11,3,5,8), produced_by(p70,11,9,10,14), produced_by(p71,15,7,14,11), produced_by(p72,15,8,3,13), produced_by(p73,2,6,7,5), produced_by(p74,2,3,9,4), produced_by(p75,10,10,13,2), produced_by(p76,10,7,14,10), produced_by(p77,6,4,14,8), produced_by(p78,13,9,13,4), produced_by(p79,15,11,14,15), produced_by(p8,12,1,8,7), produced_by(p80,4,8,4,5), produced_by(p81,6,10,1,7), produced_by(p82,12,1,10,13), produced_by(p83,3,14,14,12), produced_by(p84,13,4,6,10), produced_by(p85,8,4,2,5), produced_by(p86,4,14,15,11), produced_by(p87,2,5,2,12), produced_by(p88,12,12,8,2), produced_by(p89,6,9,15,9), produced_by(p9,5,10,14,15), produced_by(p90,1,2,6,3), produced_by(p91,15,12,6,4), produced_by(p92,15,3,13,7), produced_by(p93,14,14,3,2), produced_by(p94,5,2,4,6), produced_by(p95,13,12,2,10), produced_by(p96,8,9,3,13), produced_by(p97,9,3,13,2), produced_by(p98,4,11,4,10), produced_by(p99,7,2,14,6)}
"""
