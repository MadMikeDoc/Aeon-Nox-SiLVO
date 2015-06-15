import xbmc
import xbmcgui

if xbmc.getCondVisibility('Control.HasFocus(8001)') == 1 and (xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),1)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),4)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),20)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),40)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),41)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),42)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),43)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),44)') == 1):
	xbmc.executebuiltin("XBMC.Skin.ToggleSetting(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8052)")

if xbmc.getCondVisibility('Control.HasFocus(8001)') == 1 and (xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),2)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),5)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),7)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),8)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),9)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),21)') == 1 or xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),45)') == 1):
	xbmc.executebuiltin("XBMC.Skin.ToggleSetting(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8072)")

if xbmc.getCondVisibility('Control.HasFocus(8001)') == 1 and xbmc.getCondVisibility('StringCompare(Container(9000).ListItem.Property(WidgetType),47)') == 1:
	xbmc.executebuiltin("XBMC.Skin.ToggleSetting(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")	
	
if xbmc.getCondVisibility('Control.HasFocus(8001)') == 1 and xbmc.getCondVisibility('Skin.HasSetting(HomeInfo)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(9000)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(9000)")
	
if xbmc.getCondVisibility('Control.HasFocus(9010)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(9010)")
	
if xbmc.getCondVisibility('Control.HasFocus(8053)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8054)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")

if xbmc.getCondVisibility('Control.HasFocus(8055)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")

if xbmc.getCondVisibility('Control.HasFocus(8056)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8057)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8058)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8059)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8060)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8061)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8062)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8063)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8073)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8074)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")

if xbmc.getCondVisibility('Control.HasFocus(8075)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")

if xbmc.getCondVisibility('Control.HasFocus(8076)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8077)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8078)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")
	
if xbmc.getCondVisibility('Control.HasFocus(8079)') == 1:
	xbmc.executebuiltin("XBMC.Skin.Reset(HomeInfo)")		
	xbmc.executebuiltin("XBMC.Control.SetFocus(8001)")