# Побитый диск


**Category:** img, dmg, filesystem, admin
**Points:** 400
**Description:**

> Наш предыдущий админ попортил usb-флешку нашей сотрудницы. По её словам, там хранились очень важные для компании данные (а не просто фотографии котиков) 
> https://innoctf.hackforces.com/files/admin/400/bad_usb.dmg

## WriteUp 

Ищем тулзу для перевода dmg в img. Находим [dmg2img](http://www.softpedia.com/get/System/Hard-Disk-Utils/DMG2IMG.shtml) с [открытым кодом](https://github.com/Lekensteyn/dmg2img). Пробуем перевести, видим ошибку, ищем в репозитории и находим нужную сигнатуру. Смотрим позицию **с конца** изменяем, пробуем еще раз. В полученном img находим флаг.
