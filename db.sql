/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.14-MariaDB : Database - blk_forensic
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`blk_forensic` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `blk_forensic`;

/*Table structure for table `add_crime` */

DROP TABLE IF EXISTS `add_crime`;

CREATE TABLE `add_crime` (
  `crime_num` int(11) NOT NULL AUTO_INCREMENT,
  `station_num` int(11) NOT NULL,
  `fname` varchar(500) NOT NULL,
  `lname` varchar(550) NOT NULL,
  `designation` varchar(400) NOT NULL,
  `case_num` varchar(300) NOT NULL,
  `type_of_crime` varchar(400) NOT NULL,
  `latitude` varchar(500) NOT NULL,
  `longitude` varchar(600) NOT NULL,
  `status` varchar(600) NOT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`crime_num`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `add_crime` */

insert  into `add_crime`(`crime_num`,`station_num`,`fname`,`lname`,`designation`,`case_num`,`type_of_crime`,`latitude`,`longitude`,`status`,`date`) values (1,2,'arjun','a','CIRCLE','23658','MURDER','11.338993251466137','76.09975584413714','ASSIGN STAFF FOR EXAMINATION',NULL),(2,2,'anu','kk','CIRCLE','2358','THEFT','10.085845155835656','76.33472675365996','COLLECTION COMPLETED',NULL),(3,1,'alen','k','CIRCLE','8089','KIDNAP','9.981820779130924','76.29593271835138','pending','2022-11-19'),(4,3,'arjun','as','CIRCLE','1','KIDNAP','10.441546369368316','76.24346672026336','COLLECTION COMPLETED','2022-11-21'),(5,3,'assswwsa','qqwewe','CIRCLE','856','MURDER','9.972944855691281','76.29636187179376','ASSIGN STAFF FOR EXAMINATION','2022-11-21');

/*Table structure for table `add_forensic_staff` */

DROP TABLE IF EXISTS `add_forensic_staff`;

CREATE TABLE `add_forensic_staff` (
  `fs_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) NOT NULL,
  `fname` varchar(900) NOT NULL,
  `lname` varchar(900) NOT NULL,
  `gender` varchar(400) NOT NULL,
  `dob` varchar(500) NOT NULL,
  `state` varchar(800) NOT NULL,
  `district` varchar(600) NOT NULL,
  `city` varchar(700) NOT NULL,
  `address` varchar(750) NOT NULL,
  `pincode` varchar(400) NOT NULL,
  `phone` varchar(600) NOT NULL,
  `alt_phone` varchar(600) DEFAULT NULL,
  `email` varchar(700) NOT NULL,
  `doj` varchar(500) NOT NULL,
  `photo` varchar(600) DEFAULT NULL,
  PRIMARY KEY (`fs_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `add_forensic_staff` */

insert  into `add_forensic_staff`(`fs_id`,`login_id`,`fname`,`lname`,`gender`,`dob`,`state`,`district`,`city`,`address`,`pincode`,`phone`,`alt_phone`,`email`,`doj`,`photo`) values (1,6,'Rosmy','j','FEMALE','2000-08-25','KERALA','THIRUVANANTHAPURAM','pala','				   \r\nads			','677889','8889997707','7896541239','sasi2123@gmail.com','2022-11-19','static/ac598006-5570-4e96-bcd5-cb2378b130dfIMG_1437_92f93c80-586c-471d-b9b6-aff74f565dc7_600x.jpg'),(2,7,'Merin','jm','FEMALE','2000-02-09','KERALA','ERNAKULAM','kochi','fort kochi','682001','8089397399','','merinmariadj@gmail.com','2022-11-03','static/09de31d9-b329-4496-96f6-551f04512e7d'),(3,8,'varsha','s','MALE','2022-11-07','KERALA','ERNAKULAM','kochi','erkm','235698','7410258963','','vash@gail.com','2022-11-19','static/ddd1e17e-5705-41b0-b33b-6f698915eb98'),(4,11,'tr','tr','MALE','2022-11-11','KERALA','THIRUVANANTHAPURAM','456789','','','7896541231','','t@gmil.com','2022-11-21','static/ffccc11d-ffbd-4453-bc75-477b2ab27e43'),(5,12,'tr','tr','MALE','2022-11-11','KERALA','THIRUVANANTHAPURAM','456789','','','7896541231','','t@gmil.com','2022-11-21','static/c730a816-9582-47cf-bba0-feada552cfd0');

/*Table structure for table `assign_staff` */

DROP TABLE IF EXISTS `assign_staff`;

CREATE TABLE `assign_staff` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `fs_id` int(11) DEFAULT NULL,
  `crime_num` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `assign_staff` */

insert  into `assign_staff`(`assign_id`,`fs_id`,`crime_num`,`status`) values (2,2,1,'ASSIGN STAFF FOR EXAMINATION'),(3,2,4,'COLLECTION COMPLETED'),(4,3,5,'COLLECTION COMPLETED'),(5,5,5,'ASSIGN STAFF FOR EXAMINATION');

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attnd_id` int(11) NOT NULL AUTO_INCREMENT,
  `fs_id` int(11) NOT NULL,
  `status` varchar(400) NOT NULL,
  `date` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`attnd_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

insert  into `attendance`(`attnd_id`,`fs_id`,`status`,`date`) values (1,1,'Present','2022-11-19'),(2,2,'Present','2022-11-19'),(3,2,'Present','2022-11-21'),(4,3,'Present','2022-11-21'),(5,5,'Present','2022-11-21');

/*Table structure for table `court` */

DROP TABLE IF EXISTS `court`;

CREATE TABLE `court` (
  `court_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) NOT NULL,
  `crt_reg_num` varchar(400) NOT NULL,
  `c_name` varchar(800) NOT NULL,
  `ty_crt` varchar(400) NOT NULL,
  `state` varchar(400) NOT NULL,
  `district` varchar(400) NOT NULL,
  `addr` varchar(100) NOT NULL,
  `pin` varchar(300) NOT NULL,
  `email` varchar(500) NOT NULL,
  `phone1` varchar(400) NOT NULL,
  `phone2` varchar(400) NOT NULL,
  `officer_name` varchar(600) NOT NULL,
  PRIMARY KEY (`court_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `court` */

insert  into `court`(`court_id`,`login_id`,`crt_reg_num`,`c_name`,`ty_crt`,`state`,`district`,`addr`,`pin`,`email`,`phone1`,`phone2`,`officer_name`) values (1,4,'High court','682001','HIGH COURT','KERALA','Ernakulam','High court,Ernakulam','682100','hcKerala@gmail.com','9037686634','9370864366','Rahul'),(2,5,'ekm fmly court','808586','MUNSIF COURT','KERALA','Ernakulam','ekm fmly crt','685230','fml@gmail.com','5060708090','1020304000','arjun'),(3,10,'dist  cort way','2246','DISTRICT COURT','ANDHRA PRADESH','ekm','123lop','523641','distway@gmail.com','5236987410','9874563210','rahul');

/*Table structure for table `fingerprint` */

DROP TABLE IF EXISTS `fingerprint`;

CREATE TABLE `fingerprint` (
  `fp_id` int(11) NOT NULL AUTO_INCREMENT,
  `crime_num` int(11) NOT NULL,
  `fs_id` int(11) NOT NULL,
  `pattern` varchar(300) DEFAULT NULL,
  `ref_point` varchar(350) DEFAULT NULL,
  `met_of_coll` varchar(340) DEFAULT NULL,
  `add_info` varchar(150) DEFAULT NULL,
  `image` varchar(1500) DEFAULT NULL,
  `date_time` varchar(60) DEFAULT NULL,
  `f_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`fp_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `fingerprint` */

insert  into `fingerprint`(`fp_id`,`crime_num`,`fs_id`,`pattern`,`ref_point`,`met_of_coll`,`add_info`,`image`,`date_time`,`f_status`) values (1,1,1,'WHORLS','RIDGE REUNION','ELECTRON AUTO RADIOGRAPHY','nil						\r\n					','static/ce7c1d1e-27ac-4ad5-a0ec-dde93fba800e','2022-11-19 12:51:37','verified'),(2,4,2,'LOOP','ISLAND WITH DOT','SILVER NITRATE SOLUTION','						\r\n			4		','static/a721cda3-57d7-455f-a0e2-fe742ab8de8d','2022-11-21 19:11:51','pending');

/*Table structure for table `footprint` */

DROP TABLE IF EXISTS `footprint`;

CREATE TABLE `footprint` (
  `foot_id` int(11) NOT NULL AUTO_INCREMENT,
  `crime_num` int(11) NOT NULL,
  `fs_id` int(11) NOT NULL,
  `left_len` varchar(200) DEFAULT NULL,
  `left_width` varchar(200) DEFAULT NULL,
  `right_len` varchar(200) DEFAULT NULL,
  `right_width` varchar(200) DEFAULT NULL,
  `add_info` varchar(200) DEFAULT NULL,
  `height` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `date_time` varchar(100) DEFAULT NULL,
  `ft_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`foot_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `footprint` */

insert  into `footprint`(`foot_id`,`crime_num`,`fs_id`,`left_len`,`left_width`,`right_len`,`right_width`,`add_info`,`height`,`gender`,`date_time`,`ft_status`) values (1,1,1,'','','12','2','','84','Female','2022-11-19 12:58:28','verified');

/*Table structure for table `hair_test` */

DROP TABLE IF EXISTS `hair_test`;

CREATE TABLE `hair_test` (
  `hair_id` int(11) NOT NULL AUTO_INCREMENT,
  `crime_num` int(11) NOT NULL,
  `fs_id` int(11) NOT NULL,
  `hair_fiber` varchar(800) DEFAULT NULL,
  `dia_medu` varchar(1100) DEFAULT NULL,
  `dia_hair` varchar(1000) DEFAULT NULL,
  `which_part` varchar(700) DEFAULT NULL,
  `pre_barr_bodies` varchar(900) DEFAULT NULL,
  `animal_or_human` varchar(500) DEFAULT NULL,
  `gender` varchar(800) DEFAULT NULL,
  `ht_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`hair_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `hair_test` */

insert  into `hair_test`(`hair_id`,`crime_num`,`fs_id`,`hair_fiber`,`dia_medu`,`dia_hair`,`which_part`,`pre_barr_bodies`,`animal_or_human`,`gender`,`ht_status`) values (1,1,1,'Hair','2','10','HAIR ON SCALP','on','human hair','MALE','verified');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(60) NOT NULL,
  `usertype` varchar(40) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'pol1','pol1','POLICE'),(3,'pol2','pol2','POLICE'),(4,'court1','court1','COURT'),(5,'court2','court2','COURT'),(6,'493549','2000-08-25','FORENSIC STAFF'),(7,'784159','2000-02-09','FORENSIC STAFF'),(8,'992892','2022-11-07','FORENSIC STAFF'),(9,'way1','way1','POLICE'),(10,'waycrt','waycrt','COURT'),(11,'208205','2022-11-11','FORENSIC STAFF'),(12,'659251','2022-11-11','FORENSIC STAFF');

/*Table structure for table `police_station` */

DROP TABLE IF EXISTS `police_station`;

CREATE TABLE `police_station` (
  `station_num` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) NOT NULL,
  `st_reg_num` varchar(40) NOT NULL,
  `zone` varchar(50) NOT NULL,
  `district` varchar(60) NOT NULL,
  `city` varchar(50) NOT NULL,
  `pincode` varchar(40) NOT NULL,
  `station_name` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  `email` varchar(40) NOT NULL,
  `phone` varchar(40) NOT NULL,
  `alt_phone` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`station_num`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `police_station` */

insert  into `police_station`(`station_num`,`login_id`,`st_reg_num`,`zone`,`district`,`city`,`pincode`,`station_name`,`address`,`email`,`phone`,`alt_phone`) values (1,2,'123','NORTH ZONE','KOZHIKODE','mittai street','123456','mittai station','mittai','mittai@gmail.com','1234567890','2468135790'),(2,3,'8089','SOUTH ZONE','ERNAKULAM','kochi','682001','North Police station','north station','np@gmail.com','8089397399','8089393799'),(3,9,'9078','SOUTH ZONE','WAYANAD','tata','124562','way ps','north ps','way@gmail.com','8520258852','1234567890');

/*Table structure for table `post_mortem` */

DROP TABLE IF EXISTS `post_mortem`;

CREATE TABLE `post_mortem` (
  `pm_id` int(11) NOT NULL AUTO_INCREMENT,
  `crime_num` int(11) NOT NULL,
  `fs_id` int(11) NOT NULL,
  `body_temp` varchar(800) DEFAULT NULL,
  `changes_in_eye` varchar(500) DEFAULT NULL,
  `livor_mortis` varchar(500) DEFAULT NULL,
  `degradation` varchar(1000) DEFAULT NULL,
  `time_snc_death_in_hrs` varchar(500) DEFAULT NULL,
  `degradation_time` varchar(500) DEFAULT NULL,
  `date_time` varchar(600) DEFAULT NULL,
  `pm_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pm_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `post_mortem` */

insert  into `post_mortem`(`pm_id`,`crime_num`,`fs_id`,`body_temp`,`changes_in_eye`,`livor_mortis`,`degradation`,`time_snc_death_in_hrs`,`degradation_time`,`date_time`,`pm_status`) values (1,1,1,'24','0','INTIAL STAGE','teeth become loose','12HR -16 HOURS SINCE DEATH HAPPEN','3-5 DAYS SINCE DEATH HAPPEN','2022-11-19 13:10:37','verified');

/*Table structure for table `request_evidence` */

DROP TABLE IF EXISTS `request_evidence`;

CREATE TABLE `request_evidence` (
  `req_ev_no` int(11) NOT NULL AUTO_INCREMENT,
  `case_num` int(11) NOT NULL,
  `court_id` int(11) NOT NULL,
  `status` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`req_ev_no`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `request_evidence` */

insert  into `request_evidence`(`req_ev_no`,`case_num`,`court_id`,`status`) values (1,23658,1,'Accepted');

/*Table structure for table `teeth` */

DROP TABLE IF EXISTS `teeth`;

CREATE TABLE `teeth` (
  `teeth_id` int(11) NOT NULL AUTO_INCREMENT,
  `crime_num` int(11) NOT NULL,
  `fs_id` int(11) NOT NULL,
  `root_diver` varchar(50) DEFAULT NULL,
  `appear` varchar(60) DEFAULT NULL,
  `color` varchar(70) DEFAULT NULL,
  `edge` varchar(50) DEFAULT NULL,
  `teeth_ident` varchar(40) DEFAULT NULL,
  `temp_typ_teeth` varchar(50) DEFAULT NULL,
  `per_typ_teeth` varchar(50) DEFAULT NULL,
  `date_time` varchar(40) DEFAULT NULL,
  `t_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`teeth_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `teeth` */

insert  into `teeth`(`teeth_id`,`crime_num`,`fs_id`,`root_diver`,`appear`,`color`,`edge`,`teeth_ident`,`temp_typ_teeth`,`per_typ_teeth`,`date_time`,`t_status`) values (1,1,1,'yes','SMALL LIGHT & NARROW','MILKY WHITE','SMOOTH CUTTING ','TEMPORARY','LATERAL MOLARS','FIRST MOLAR','2022-11-19 13:06:47','verified');

/*Table structure for table `video_audio` */

DROP TABLE IF EXISTS `video_audio`;

CREATE TABLE `video_audio` (
  `va_id` int(11) NOT NULL AUTO_INCREMENT,
  `fs_id` int(11) NOT NULL,
  `crime_num` int(11) NOT NULL,
  `audio` varchar(5000) DEFAULT NULL,
  `video` varchar(5000) DEFAULT NULL,
  `date_time` varchar(500) DEFAULT NULL,
  `va_status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`va_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `video_audio` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
