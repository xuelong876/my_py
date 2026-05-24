========================================
   uiautomation (Windows°æ) ºËĞÄ²Î¿¼ÊÖ²á
========================================

¡¾Ò»¡¢³£ÓÃ¿Ø¼şÀà¡¿

1. WindowControl - ´ú±íÓ¦ÓÃµÄÖ÷´°¿Ú»ò×Ó´°¿Ú
   - ÓÃÍ¾£ºÕÒµ½´°¿Ú£¬×÷ÎªÆäËû¿Ø¼ş²éÕÒµÄÆğµã
   - Ê¾Àı£ºwindow = WindowControl(Name='¼ÆËãÆ÷')

2. ButtonControl - ¸÷Àà°´Å¥
   - ÓÃÍ¾£ºµã»÷È·¶¨¡¢È¡Ïû¡¢¹Ø±ÕµÈ°´Å¥
   - Ê¾Àı£ºbutton = window.ButtonControl(Name='È·¶¨')

3. EditControl - ÎÄ±¾ÊäÈë¿ò£¨µ¥ĞĞ/¶àĞĞ£©
   - ÓÃÍ¾£ºÊäÈëÓÃ»§Ãû¡¢ÃÜÂëµÈÎÄ±¾
   - Ê¾Àı£ºedit = window.EditControl(Name='ÓÃ»§Ãû')

4. TextControl - ¾²Ì¬ÎÄ±¾±êÇ©
   - ÓÃÍ¾£º»ñÈ¡½çÃæÌáÊ¾ÎÄ×Ö»ò´íÎóĞÅÏ¢
   - Ê¾Àı£ºtext = window.TextControl(Name='»¶Ó­')

5. ComboBoxControl - ÏÂÀ­Ñ¡Ôñ¿ò
   - ÓÃÍ¾£ºÑ¡ÔñÏÂÀ­²Ëµ¥ÖĞµÄÑ¡Ïî
   - Ê¾Àı£ºcombo = window.ComboBoxControl(Name='Ê¡·İ')

6. ListItemControl - ÁĞ±í¿òÖĞµÄÏîÄ¿
   - ÓÃÍ¾£ºÔÚÁĞ±í»òÏÂÀ­¿òÖĞÑ¡ÖĞÄ³Ïî
   - Ê¾Àı£ºitem = window.ListItemControl(Name='±±¾©')

7. MenuItemControl - ²Ëµ¥Ïî
   - ÓÃÍ¾£ºµã»÷ÎÄ¼ş->Áí´æÎªµÈ²Ëµ¥
   - Ê¾Àı£ºmenu = window.MenuItemControl(Name='±£´æ')

8. CheckBoxControl - ¸´Ñ¡¿ò
   - ÓÃÍ¾£º¹´Ñ¡»òÈ¡Ïû¹´Ñ¡Ñ¡Ïî
   - Ê¾Àı£ºcheckbox = window.CheckBoxControl(Name='¼Ç×¡ÃÜÂë')

9. RadioButtonControl - µ¥Ñ¡°´Å¥
   - ÓÃÍ¾£ºµ¥Ñ¡Ñ¡Ïî
   - Ê¾Àı£ºradio = window.RadioButtonControl(Name='ÄĞ')

10. TabControl - Ñ¡Ïî¿¨¿Ø¼ş
    - ÓÃÍ¾£ºÇĞ»»²»Í¬±êÇ©Ò³
    - Ê¾Àı£ºtab = window.TabControl(Name='ÉèÖÃ')

11. ListControl - ÁĞ±í¿Ø¼ş
    - ÓÃÍ¾£º²Ù×÷ÁĞ±íÖĞµÄËùÓĞÏîÄ¿
    - Ê¾Àı£ºlist = window.ListControl()

12. TreeControl - Ê÷ĞÎ¿Ø¼ş
    - ÓÃÍ¾£º²Ù×÷Ê÷ĞÎ½á¹¹µÄÄ¿Â¼
    - Ê¾Àı£ºtree = window.TreeControl()

13. TableControl - ±í¸ñ¿Ø¼ş
    - ÓÃÍ¾£º²Ù×÷±í¸ñÊı¾İ
    - Ê¾Àı£ºtable = window.TableControl()

14. HyperlinkControl - ³¬Á´½Ó
    - ÓÃÍ¾£ºµã»÷Á´½Ó
    - Ê¾Àı£ºlink = window.HyperlinkControl(Name='ÁË½â¸ü¶à')

15. ImageControl - Í¼Æ¬¿Ø¼ş
    - ÓÃÍ¾£º»ñÈ¡»ò²Ù×÷Í¼Æ¬
    - Ê¾Àı£ºimage = window.ImageControl()


¡¾¶ş¡¢ºËĞÄ·½·¨¡¿

1. ²éÕÒ¿Ø¼ş·½·¨£º
   - Control(searchDepth, ClassName, Name, AutomationId)
   - WindowControl(searchDepth, ClassName, Name, AutomationId)
   - ButtonControl(searchDepth, ClassName, Name, AutomationId)
   µÈµÈ...Ã¿¸ö¿Ø¼şÀà¶¼ÓĞÏàÍ¬µÄ²éÕÒ²ÎÊı

2. ³£ÓÃ²Ù×÷£º
   - Click()           # µ¥»÷¿Ø¼ş
   - RightClick()      # ÓÒ¼üµ¥»÷
   - DoubleClick()     # Ë«»÷¿Ø¼ş
   - SetValue(text)    # ÉèÖÃÖµ£¨ÊäÈë¿ò£©
   - GetValue()        # »ñÈ¡¿Ø¼şÖµ
   - SendKeys(text)    # Ä£Äâ¼üÅÌÊäÈë
   - Select(itemName)  # Ñ¡ÔñÏî£¨ÏÂÀ­¿ò/ÁĞ±í£©
   - Exists()          # ¼ì²é¿Ø¼şÊÇ·ñ´æÔÚ
   - Close()           # ¹Ø±Õ´°¿Ú
   - Maximize()        # ×î´ó»¯´°¿Ú
   - Minimize()        # ×îĞ¡»¯´°¿Ú
   - Restore()         # »Ö¸´´°¿Ú
   - GetParent()       # »ñÈ¡¸¸¿Ø¼ş
   - GetChildren()     # »ñÈ¡ËùÓĞ×Ó¿Ø¼ş
   - GetFirstChild()   # »ñÈ¡µÚÒ»¸ö×Ó¿Ø¼ş
   - GetLastChild()    # »ñÈ¡×îºóÒ»¸ö×Ó¿Ø¼ş
   - SetFocus()        # ÉèÖÃ½¹µãµ½¿Ø¼ş

3. µÈ´ı·½·¨£º
   - WaitForExist(timeout=3)     # µÈ´ı¿Ø¼ş³öÏÖ
   - WaitForEnabled(timeout=3)   # µÈ´ı¿Ø¼şÆôÓÃ
   - WaitForControl(timeout=3)   # µÈ´ı¿Ø¼ş¿ÉÓÃ

4. ÊôĞÔ»ñÈ¡£º
   - Name              # ¿Ø¼şµÄÃû³Æ
   - AutomationId      # ¿Ø¼şµÄ×Ô¶¯»¯ID
   - ClassName         # ¿Ø¼şµÄÀàÃû
   - ControlType       # ¿Ø¼şÀàĞÍ
   - BoundingRectangle # ¿Ø¼şµÄ±ß½ç¾ØĞÎ
   - IsEnabled         # ÊÇ·ñÆôÓÃ
   - IsVisible         # ÊÇ·ñ¿É¼û
   - ProcessId         # ½ø³ÌID


¡¾Èı¡¢¹Ø¼ü²éÕÒ²ÎÊı¡¿

³£ÓÃµÄ¶¨Î»²ÎÊı£¨°´ÍÆ¼öÓÅÏÈ¼¶ÅÅĞò£©£º
1. AutomationId  # ×î¿É¿¿£¬¿ª·¢ÕßÖ¸¶¨µÄÎ¨Ò»ID
2. Name          # ¿Ø¼şµÄÎÄ±¾Ãû³Æ
3. ClassName     # ¿Ø¼şµÄÀàÃû
4. ControlType   # ¿Ø¼şÀàĞÍ
5. Depth         # ËÑË÷Éî¶È
6. Index         # Í¬¼¶¿Ø¼şË÷Òı

Ê¾Àı£º
button = window.ButtonControl(AutomationId='btnOK', Name='È·¶¨')


¡¾ËÄ¡¢ÊµÓÃÊ¾Àı´úÂë¡¿

1. Æô¶¯Ó¦ÓÃ²¢»ñÈ¡´°¿Ú£º
   import uiautomation as auto
   auto.UIAutomation()
   
   # Æô¶¯¼ÇÊÂ±¾
   auto.SendKeys('notepad')
   auto.SendKeys('{Enter}')
   
   # »ñÈ¡´°¿Ú
   notepad = auto.WindowControl(Name='ÎŞ±êÌâ - ¼ÇÊÂ±¾')

2. ²éÕÒ²¢²Ù×÷¿Ø¼ş£º
   # ²éÕÒ±à¼­¿ò²¢ÊäÈëÎÄ×Ö
   edit = notepad.EditControl()
   edit.SetValue('Hello World')
   
   # µã»÷±£´æ°´Å¥
   save_btn = notepad.ButtonControl(Name='±£´æ')
   save_btn.Click()

3. µÈ´ı¿Ø¼ş³öÏÖ£º
   dialog = auto.WindowControl(Name='Áí´æÎª')
   if dialog.WaitForExist(5):
       file_name = dialog.EditControl(Name='ÎÄ¼şÃû')
       file_name.SetValue('test.txt')
       dialog.ButtonControl(Name='±£´æ').Click()

4. ±éÀúËùÓĞ×Ó¿Ø¼ş£º
   for control in window.GetChildren():
       print(f'Ãû³Æ: {control.Name}, ÀàĞÍ: {control.ControlTypeName}')

5. ´¦Àí²Ëµ¥£º
   menu = window.MenuItemControl(Name='ÎÄ¼ş')
   menu.Click()
   sub_menu = window.MenuItemControl(Name='Áí´æÎª')
   sub_menu.Click()


¡¾Îå¡¢ÖØÒª¹Ø¼üµã¡¿

1. ±ØĞëÏÈµ¼Èë¿â£º
   import uiautomation as auto

2. ³õÊ¼»¯UIAutomation£¨¿ÉÑ¡µ«ÍÆ¼ö£©£º
   auto.UIAutomation()

3. ²éÕÒ¿Ø¼şµÄ²ã¼¶½á¹¹£º
   Í¨³£´ÓWindowControl¿ªÊ¼£¬Öğ¼¶ÏòÏÂ²éÕÒ×Ó¿Ø¼ş

4. Î¨Ò»±êÊ¶ÓÅÏÈÊ¹ÓÃ£º
   AutomationId > Name > ClassName

5. ÉèÖÃÈ«¾ÖËÑË÷³¬Ê±£º
   auto.SetGlobalSearchTimeout(3)  # 3Ãë³¬Ê±

6. ¿Ø¼ş»º´æÓÅ»¯ĞÔÄÜ£º
   auto.SetGlobalCacheTime(1.0)    # »º´æ1Ãë

7. µ÷ÊÔÓÃ¿ª¹Ø£º
   auto.SetGlobalDebug(True)       # ¿ªÆôµ÷ÊÔÊä³ö
   auto.ShowDesktop()              # ÏÔÊ¾×ÀÃæÉÏµÄËùÓĞ¿Ø¼ş

8. ¼üÅÌÊó±êÄ£Äâ£º
   auto.SendKeys('{Ctrl}C')        # ¸´ÖÆ
   auto.SendKeys('{Ctrl}V')        # Õ³Ìù
   auto.SendKeys('{Enter}')        # »Ø³µ
   auto.MoveTo(x, y)               # ÒÆ¶¯Êó±ê
   auto.Click(x, y)                # µã»÷×ø±ê

9. ½ØÍ¼¹¦ÄÜ£º
   control.CaptureToImage('screenshot.png')  # ½ØÈ¡¿Ø¼şÇøÓò

10. ¹ö¶¯²Ù×÷£º
    control.SetScrollPercent(horizontal, vertical)  # ¹ö¶¯µ½Ö¸¶¨Î»ÖÃ
    control.Scroll(horizontalAmount, verticalAmount) # ¹ö¶¯Ö¸¶¨Á¿


¡¾Áù¡¢³£ÓÃ¸¨Öúº¯Êı¡¿

1. GetRootControl()        # »ñÈ¡¸ù¿Ø¼ş£¨×ÀÃæ£©
2. GetForegroundWindow()   # »ñÈ¡µ±Ç°Ç°Ì¨´°¿Ú
3. GetFocusedControl()     # »ñÈ¡µ±Ç°½¹µã¿Ø¼ş
4. GetCursorPos()          # »ñÈ¡Êó±êÎ»ÖÃ
5. SetCursorPos(x, y)      # ÉèÖÃÊó±êÎ»ÖÃ
6. MessageBox(text, title) # ÏÔÊ¾ÏûÏ¢¿ò
7. WalkControl(control)    # ±éÀúËùÓĞ¿Ø¼şÊ÷


¡¾Æß¡¢×î¼ÑÊµ¼ù½¨Òé¡¿

1. Ìí¼ÓÊÊµ±µÄµÈ´ıÊ±¼ä£¬±ÜÃâ¿Ø¼şÎ´¼ÓÔØ¾Í²Ù×÷
2. ÓÅÏÈÊ¹ÓÃAutomationId£¬ËüÊÇ¶¨Î»×îÎÈ¶¨µÄ·½Ê½
3. ·â×°³£ÓÃµÄ¿Ø¼ş²Ù×÷Îªº¯Êı£¬Ìá¸ß´úÂë¸´ÓÃĞÔ
4. Òì³£´¦ÀíºÜÖØÒª£¬ÓÃtry-catch°ü¹ü²Ù×÷
5. ¸´ÔÓ²Ù×÷Ç°ÏÈ¼ì²é¿Ø¼şÊÇ·ñ´æÔÚºÍ¿ÉÓÃ
6. Ê¹ÓÃÏà¶ÔÂ·¾¶²éÕÒ£¬²»Òª¹ı¶ÈÒÀÀµ¾ø¶ÔÂ·¾¶
7. ¶¨ÆÚÇåÀí²»ÔÙÊ¹ÓÃµÄ¿Ø¼şÒıÓÃ£¬ÊÍ·ÅÄÚ´æ
8. ´óÅúÁ¿²Ù×÷Ê±Ê¹ÓÃ»º´æÌá¸ßĞÔÄÜ


¡¾°Ë¡¢×¢ÒâÊÂÏî¡¿

1. Ä³Ğ©Ó¦ÓÃĞèÒª¹ÜÀíÔ±È¨ÏŞ²ÅÄÜ×Ô¶¯»¯
2. ĞéÄâ×ÀÃæ»òÔ¶³Ì×ÀÃæ¿ÉÄÜÓ°Ïì¿Ø¼şÊ¶±ğ
3. ²»Í¬Windows°æ±¾µÄ¿Ø¼şÊôĞÔ¿ÉÄÜÓĞ²îÒì
4. Ä³Ğ©ÀÏ¾ÉÓ¦ÓÃ¿ÉÄÜ²»ÍêÈ«Ö§³ÖUI Automation API
5. ¿Ø¼ş´°¿Ú¹Ø±Õºó£¬¶ÔÓ¦µÄControl¶ÔÏó»áÊ§Ğ§

========================================
   WindowControl.SwitchToThisWindow() ·½·¨Ïê½â
========================================


¡¾Ò»¡¢·½·¨»ù±¾ËµÃ÷¡¿

·½·¨Ãû³Æ£ºSwitchToThisWindow()
ËùÊôÀà£ºWindowControl
¹¦ÄÜËµÃ÷£º½«Ö¸¶¨´°¿ÚÇĞ»»µ½Ç°Ì¨²¢¼¤»îËü
×îÖÕĞ§¹û£º´°¿Ú»áÏÔÊ¾ÔÚ×îÉÏ²ã£¬²¢»ñµÃÊäÈë½¹µã


¡¾¶ş¡¢»ù´¡Óï·¨¡¿

import uiautomation as auto

# »ñÈ¡´°¿Ú¶ÔÏó
window = auto.WindowControl(Name="´°¿Ú±êÌâ")

# ½«´°¿ÚÇĞ»»µ½Ç°Ì¨
window.SwitchToThisWindow()


¡¾Èı¡¢Êµ¼ÊÓ¦ÓÃÊ¾Àı¡¿

Ê¾Àı1£ºÎ¢ĞÅ×Ô¶¯»¯£¨³£¼û³¡¾°£©

import uiautomation as auto

# »ñÈ¡Î¢ĞÅÖ÷´°¿Ú
wx = auto.WindowControl(ClassName="WeChatMainWndForPC", Name="Î¢ĞÅ", searchDepth=1)

# ÇĞ»»µ½Î¢ĞÅ´°¿Ú£¨È·±£ºóĞø²Ù×÷ÔÚÕıÈ·´°¿ÚÖĞÖ´ĞĞ£©
wx.SwitchToThisWindow()

# È»ºóÖ´ĞĞÆäËû²Ù×÷
txl_btn = wx.ButtonControl(Name="Í¨Ñ¶Â¼")
txl_btn.Click()


Ê¾Àı2£º²Ù×÷¼ÇÊÂ±¾

import uiautomation as auto

# »ñÈ¡¼ÇÊÂ±¾´°¿Ú
notepad = auto.WindowControl(Name="ÎŞ±êÌâ - ¼ÇÊÂ±¾", searchDepth=1)

# È·±£¼ÇÊÂ±¾ÔÚ×îÇ°Ãæ
notepad.SwitchToThisWindow()

# ÊäÈëÎÄ×Ö
edit = notepad.EditControl()
edit.SetValue("Hello World")

# µã»÷±£´æ°´Å¥
save_btn = notepad.ButtonControl(Name="±£´æ")
save_btn.Click()


Ê¾Àı3£º¶à´°¿ÚÇĞ»»

import uiautomation as auto

# »ñÈ¡¶à¸ö´°¿Ú
calc = auto.WindowControl(Name="¼ÆËãÆ÷")
notepad = auto.WindowControl(Name="¼ÇÊÂ±¾")

# ÇĞ»»µ½¼ÆËãÆ÷
calc.SwitchToThisWindow()
calc.ButtonControl(Name="1").Click()

# ÇĞ»»µ½¼ÇÊÂ±¾
notepad.SwitchToThisWindow()
notepad.EditControl().SetValue("¼ÆËã½á¹û£º1")


¡¾ËÄ¡¢ÓëÆäËû·½·¨µÄÇø±ğ¶Ô±È¡¿

·½·¨Ãû³Æ              | ¹¦ÄÜËµÃ÷                          | Ê¹ÓÃ³¡¾°
---------------------|-----------------------------------|-------------------
SwitchToThisWindow() | ÁÙÊ±½«´°¿ÚÇĞ»»µ½Ç°Ì¨              | È·±£´°¿Ú¼¤»îºóÔÙ²Ù×÷
SetTopmost(True)     | ½«´°¿ÚÉèÖÃÎªÊ¼ÖÕÖÃ¶¥              | ĞèÒª´°¿ÚÒ»Ö±±£³ÖÔÚ×îÉÏ²ã
SetFocus()           | ½öÉèÖÃÊäÈë½¹µã                    | ²»ĞèÒª´°¿ÚÇ°ÖÃ£¬Ö»Ğè½¹µã
Maximize()           | ×î´ó»¯´°¿Ú                        | ĞèÒªÈ«ÆÁ²Ù×÷
Minimize()           | ×îĞ¡»¯´°¿Ú                        | ÔİÊ±Òş²Ø´°¿Ú


¡¾Îå¡¢ÖØÒª×¢ÒâÊÂÏî¡¿

1. ±ØĞëÏÈ³É¹¦»ñÈ¡´°¿Ú¶ÔÏó²ÅÄÜµ÷ÓÃ´Ë·½·¨
    ÕıÈ·£º
     window = auto.WindowControl(Name="ÎÒµÄ´°¿Ú")
     if window.Exists(3):
         window.SwitchToThisWindow()
   
    ´íÎó£º
     auto.WindowControl(Name="ÎÒµÄ´°¿Ú").SwitchToThisWindow()  # Î´¼ì²éÊÇ·ñ´æÔÚ

2. ´°¿Ú¿ÉÄÜ±»ÆäËûÓ¦ÓÃÕÚµ²
   - ¼´Ê¹µ÷ÓÃÁËSwitchToThisWindow()£¬Ä³Ğ©Ó¦ÓÃ³ÌĞò»òÏµÍ³µ¯´°ÈÔ¿ÉÄÜÇÀÕ¼½¹µã
   - ½¨ÒéÅäºÏSetTopmost()Ê¹ÓÃÌá¸ß¿É¿¿ĞÔ

3. ½¨ÒéÅäºÏExists()Ê¹ÓÃ
   if window.Exists(3):  # µÈ´ı3Ãë
       window.SwitchToThisWindow()
   else:
       print("´°¿ÚÎ´ÕÒµ½")

4. ÓëSetTopmost()µÄÇø±ğ
   - SwitchToThisWindow()£ºÁÙÊ±ÇĞ»»£¬ºóĞø¿ÉÄÜ±»ÆäËû´°¿Ú¸²¸Ç
   - SetTopmost(True)£ºÇ¿ÖÆÖÃ¶¥£¬Ê¼ÖÕ±£³Ö×îÇ°


¡¾Áù¡¿³£ÓÃ´°¿Ú²Ù×÷·½·¨»ã×Ü

import uiautomation as auto

window = auto.WindowControl(Name="´°¿Ú±êÌâ")

# ´°¿Ú¹ÜÀí·½·¨
window.SwitchToThisWindow()     # ÇĞ»»µ½Ç°Ì¨
window.SetTopmost(True)          # ÉèÖÃ´°¿ÚÖÃ¶¥
window.SetTopmost(False)         # È¡Ïû´°¿ÚÖÃ¶¥
window.Maximize()                # ×î´ó»¯
window.Minimize()                # ×îĞ¡»¯
window.Restore()                 # »Ö¸´´°¿Ú£¨´Ó×îĞ¡»¯/×î´ó»¯»Ö¸´£©
window.Close()                   # ¹Ø±Õ´°¿Ú
window.SetFocus()                # ÉèÖÃ½¹µã


¡¾Æß¡¢×î¼ÑÊµ¼ù½¨Òé¡¿

1. Ã¿´ÎÇĞ»»Ä¿±ê´°¿ÚÇ°¶¼µ÷ÓÃSwitchToThisWindow()
   ¡ú È·±£²Ù×÷·¢ËÍµ½ÕıÈ·µÄÄ¿±ê´°¿Ú

2. ÓëExists()×éºÏÊ¹ÓÃ¸ü°²È«
   ¡ú ±ÜÃâÒò´°¿Ú²»´æÔÚµ¼ÖÂ³ÌĞò±ÀÀ£

3. ÅäºÏtime.sleep()Ê¹ÓÃ
   import time
   window.SwitchToThisWindow()
   time.sleep(0.5)  # µÈ´ı´°¿ÚÇĞ»»Íê³É
   # Ö´ĞĞºóĞø²Ù×÷

4. ÔÚÎ¢ĞÅµÈ¸´ÔÓÓ¦ÓÃÖĞÌØ±ğÖØÒª
   ¡ú Î¢ĞÅ×Ô¶¯»¯±ØĞëÏÈ½«Î¢ĞÅ´°¿ÚÇĞ»»ÖÁÇ°Ì¨²ÅÄÜÕÒµ½×Ó¿Ø¼ş


¡¾°Ë¡¢ºËĞÄÒªµã×Ü½á¡¿

 SwitchToThisWindow()ÊÇÊµÏÖ´°¿Ú×Ô¶¯»¯²Ù×÷Ç°µÄ¹Ø¼ü×¼±¸²½Öè
 ËüÈ·±£ºóĞøµÄ²éÕÒºÍ²Ù×÷Ö¸Áî·¢ËÍµ½ÕıÈ·µÄÄ¿±ê´°¿Ú
 ±ÜÃâÒò´°¿ÚÎ´¼¤»îµ¼ÖÂµÄ×Ô¶¯»¯Ê§°Ü
 ±àĞ´¶à´°¿ÚÇĞ»»½Å±¾Ê±£¬½¨ÒéÃ¿´Î¸ü»»²Ù×÷´°¿ÚÇ°¶¼µ÷ÓÃ´Ë·½·¨



========================================
             ÎÄµµ½áÊø
========================================