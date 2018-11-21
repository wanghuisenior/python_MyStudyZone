/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50703
 Source Host           : localhost:3306
 Source Schema         : mystudyzone

 Target Server Type    : MySQL
 Target Server Version : 50703
 File Encoding         : 65001

 Date: 21/11/2018 09:02:32
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

use mystudyzone;
-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add permission', 1, 'add_permission');
INSERT INTO `auth_permission` VALUES (2, 'Can change permission', 1, 'change_permission');
INSERT INTO `auth_permission` VALUES (3, 'Can delete permission', 1, 'delete_permission');
INSERT INTO `auth_permission` VALUES (4, 'Can add group', 2, 'add_group');
INSERT INTO `auth_permission` VALUES (5, 'Can change group', 2, 'change_group');
INSERT INTO `auth_permission` VALUES (6, 'Can delete group', 2, 'delete_group');
INSERT INTO `auth_permission` VALUES (7, 'Can add user', 3, 'add_user');
INSERT INTO `auth_permission` VALUES (8, 'Can change user', 3, 'change_user');
INSERT INTO `auth_permission` VALUES (9, 'Can delete user', 3, 'delete_user');
INSERT INTO `auth_permission` VALUES (10, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (11, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (12, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (13, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (14, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (15, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (16, 'Can add user', 6, 'add_user');
INSERT INTO `auth_permission` VALUES (17, 'Can change user', 6, 'change_user');
INSERT INTO `auth_permission` VALUES (18, 'Can delete user', 6, 'delete_user');
INSERT INTO `auth_permission` VALUES (19, 'Can view permission', 1, 'view_permission');
INSERT INTO `auth_permission` VALUES (20, 'Can view group', 2, 'view_group');
INSERT INTO `auth_permission` VALUES (21, 'Can view user', 3, 'view_user');
INSERT INTO `auth_permission` VALUES (22, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (23, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view user', 6, 'view_user');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (2, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (1, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (6, 'study', 'user');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2018-09-14 03:25:23.416066');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2018-09-14 03:25:25.218741');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2018-09-14 03:25:35.806613');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2018-09-14 03:25:36.734659');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2018-09-14 03:25:37.821402');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2018-09-14 03:25:37.868303');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2018-09-14 03:25:38.581776');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2018-09-14 03:25:38.626657');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2018-09-14 03:25:38.675907');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2018-09-14 03:25:39.679286');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2018-09-14 03:25:40.904306');
INSERT INTO `django_migrations` VALUES (12, 'sessions', '0001_initial', '2018-09-14 03:25:41.665081');
INSERT INTO `django_migrations` VALUES (13, 'study', '0001_initial', '2018-09-14 06:17:30.728499');
INSERT INTO `django_migrations` VALUES (14, 'study', '0002_user_user_info', '2018-09-17 10:06:08.497812');
INSERT INTO `django_migrations` VALUES (15, 'study', '0003_user_image', '2018-11-21 09:00:33.868909');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for study_user
-- ----------------------------
DROP TABLE IF EXISTS `study_user`;
CREATE TABLE `study_user`  (
  `user_id` char(32) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_tel` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_email` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  `user_info` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `image` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Compact;

-- ----------------------------
-- Records of study_user
-- ----------------------------
INSERT INTO `study_user` VALUES ('01a608c6280d4953b89c7f9cf1e8796b', '雍淑兰', '14545685541', 'moyan@gc.cn', '2018-11-21 09:01:55.449671', '2018-11-21 09:01:55.449671', '合联电子信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('01da08bc9eda47629f92cd28fec9cb7d', '伊佳', '15129172022', 'okong@yahoo.com', '2018-11-21 09:01:56.860549', '2018-11-21 09:01:56.860549', '济南亿次元信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('03d8b88a9dbd4d969140fff901233df7', '子桂香', '14514600355', 'fang47@qiangliu.cn', '2018-11-21 09:01:58.210848', '2018-11-21 09:01:58.210848', '太极信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('04344f5c7a304e32bf6c3a0ed75eba4b', '笪玉梅', '15592339173', 'junshi@gmail.com', '2018-11-21 09:01:57.610644', '2018-11-21 09:01:57.610644', '艾提科信网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('069cc03ead364ddba3de59787edeb57a', '管彬', '14541263421', 'itao@91.cn', '2018-11-21 09:01:58.491755', '2018-11-21 09:01:58.491755', '兰金电子网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('0852ae7a0fad406c9aef467cce8b5f13', '敖瑞', '18823577791', 'qiang43@mp.cn', '2018-11-21 09:01:56.285907', '2018-11-21 09:01:56.285907', '易动力信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('0bb03da1863b4b7ba1795202d8a1bd58', '贝欢', '13858679563', 'chao06@hotmail.com', '2018-11-21 09:01:58.419000', '2018-11-21 09:01:58.419000', '立信电子信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('0c1d51445a9f4d528acbfad7e173b7ef', '石桂荣', '15628848382', 'leilin@hotmail.com', '2018-11-21 09:01:56.624787', '2018-11-21 09:01:56.624787', '九方信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('10e64c71a6bc40c587de56d445530ff2', '盛静', '13270069555', 'wei65@jiejun.com', '2018-11-21 09:01:58.032978', '2018-11-21 09:01:58.032978', '恩悌网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('111e35cc1e07453ca37cdc78e385e43a', '闻秀云', '15943351559', 'jingzheng@87.cn', '2018-11-21 09:01:56.236026', '2018-11-21 09:01:56.236026', '新宇龙信息网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('1475679d8947434aa3cbaeaf181dd5cf', '丘秀云', '14501708820', 'wfang@gmail.com', '2018-11-21 09:01:56.811678', '2018-11-21 09:01:56.811678', '浙大万朋传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('195da2ae5fda4299a0676c0e5cff16b8', '边文', '18073857153', 'shixiulan@gmail.com', '2018-11-21 09:01:58.719120', '2018-11-21 09:01:58.719120', '商软冠联科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('1b6e42c8dab34a39b43bc6e318002c50', '葛晶', '14579494868', 'laimin@qiangdong.net', '2018-11-21 09:01:58.260835', '2018-11-21 09:01:58.260835', '盟新传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('1c9a9d8c0c494502be7375cf8a5597df', '夏林', '18172843574', 'caiyan@hotmail.com', '2018-11-21 09:01:58.282309', '2018-11-21 09:01:58.282309', '雨林木风计算机传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('1d510bb03f4e4839b035409d33224fd1', '爱成', '13371445971', 'vwu@yahoo.com', '2018-11-21 09:01:58.333173', '2018-11-21 09:01:58.333173', '创亿网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('1f958ff144824ee38aa22455f9b42658', '郗丽', '13324232333', 'pingshao@yahoo.com', '2018-11-21 09:01:57.983739', '2018-11-21 09:01:57.983739', '数字100传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('226ae61c255b45098002129f6c4beb5a', '缪凯', '13950158368', 'dongjing@taoguiying.cn', '2018-11-21 09:01:58.310235', '2018-11-21 09:01:58.310235', '开发区世创网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('245fe31582e5490b8c97bdda5ef5afe0', '暨晨', '13505257002', 'jundong@zhong.cn', '2018-11-21 09:01:58.468811', '2018-11-21 09:01:58.468811', '方正科技信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('271d625e282f446894b8e9e3c5cd4a44', '公云', '15196352306', 'qiang07@li.cn', '2018-11-21 09:01:57.860978', '2018-11-21 09:01:57.860978', '晖来计算机信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('2804d76d4ee04d8f89f5c4ca167daeb8', '太萍', '13557569851', 'iyao@hotmail.com', '2018-11-21 09:01:57.011242', '2018-11-21 09:01:57.011242', '毕博诚科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('2a12a2007abe49e19a45262da340e600', '楚辉', '18633080163', 'yan20@gmail.com', '2018-11-21 09:01:55.377829', '2018-11-21 09:01:55.377829', '华泰通安科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('2efbea7d553a436c94dd063acfcb362c', '詹想', '15863453773', 'xiuyingyan@hotmail.com', '2018-11-21 09:01:57.633582', '2018-11-21 09:01:57.633582', '开发区世创科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('2fb17400d55f4f9f9a181ea68571f1ff', '钦璐', '13097447638', 'fma@yahoo.com', '2018-11-21 09:01:58.060966', '2018-11-21 09:01:58.060966', '济南亿次元传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('3260030aedfd45bb91339214655301ab', '魏晨', '18533626874', 'bzhou@gmail.com', '2018-11-21 09:01:58.391040', '2018-11-21 09:01:58.391040', '佳禾科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('33aae1966e2c466a8ba486f140939834', '关兰英', '15857610300', 'yongwu@hotmail.com', '2018-11-21 09:01:57.533849', '2018-11-21 09:01:57.533905', '四通传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('36770ebaf44d49a3b1e69a730e77b6a9', '况建国', '14708900852', 'nfang@hotmail.com', '2018-11-21 09:01:56.353369', '2018-11-21 09:01:56.353369', '惠派国际公司科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('39da593cd4e8455cbd169697250c26bd', '索宁', '15960190323', 'jun43@ren.cn', '2018-11-21 09:01:57.735526', '2018-11-21 09:01:57.735526', '创汇网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('490d4887321448dcbaa0df82cf2896e8', '邰彬', '18604063825', 'wuli@chao.cn', '2018-11-21 09:01:57.132920', '2018-11-21 09:01:57.132920', '银嘉科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('4ab1f68d8e454a889a0586247238e8fa', '黄涛', '15828183043', 'pguo@hotmail.com', '2018-11-21 09:01:56.883490', '2018-11-21 09:01:56.883490', '易动力信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('4ac00f12f2e7420fb2fc13c1edbb4e01', '秋璐', '18624585060', 'qiuli@xiuyingluo.cn', '2018-11-21 09:01:57.160845', '2018-11-21 09:01:57.160845', '襄樊地球村科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('538dab918b104eaa9e7d3ae2a162512f', '幸静', '13924257094', 'xiuying05@yahoo.com', '2018-11-21 09:01:58.619546', '2018-11-21 09:01:58.619546', '雨林木风计算机网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('541a8ecb07f44e558bafbf874e827ff7', '冯敏', '15683600808', 'yangtan@hotmail.com', '2018-11-21 09:01:57.411176', '2018-11-21 09:01:57.411176', '恩悌科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('57677f40d3e1497592bcd5ba10799fa8', '熊海燕', '13460186011', 'juan21@gmail.com', '2018-11-21 09:01:58.741078', '2018-11-21 09:01:58.741078', '易动力网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('5b55188bb41949608f6343ad7129e00c', '侯小红', '15258839637', 'zhaoxiulan@hotmail.com', '2018-11-21 09:01:57.461095', '2018-11-21 09:01:57.461095', '万迅电脑网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('603ab699c9f14c3aa87fc992a2ed6093', '仰雷', '15195410722', 'weili@bo.cn', '2018-11-21 09:01:57.232654', '2018-11-21 09:01:57.232654', 'MBP软件传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('61207353a33c49fb8268426469f9d246', '危彬', '15916607558', 'li32@wei.net', '2018-11-21 09:01:57.561771', '2018-11-21 09:01:57.561771', '戴硕电子网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('64ecebc0f6ae4d04b06282f2007e16cf', '辛丽娟', '15390682568', 'yong34@qiangyong.net', '2018-11-21 09:01:58.641293', '2018-11-21 09:01:58.641293', 'MBP软件信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('65cc99e32633450fb4601c2e6d0e4af1', '郗琳', '13175864643', 'taocai@hotmail.com', '2018-11-21 09:01:58.541012', '2018-11-21 09:01:58.541012', '趋势科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('687af13c574f458698cd0941ef2c4d31', '黎丽华', '18912262118', 'jie90@hotmail.com', '2018-11-21 09:01:56.833668', '2018-11-21 09:01:56.833668', '网新恒天网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('687bdd83e4234f87844db3be0ec35105', '赏淑珍', '13012195747', 'pengfang@qiangzheng.cn', '2018-11-21 09:01:56.416956', '2018-11-21 09:01:56.416956', '彩虹传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('68b607cbae9841c6aa2db5c7a65e7dc6', '靳东', '15898737822', 'mingyuan@guiying.cn', '2018-11-21 09:01:57.510943', '2018-11-21 09:01:57.510943', '恩悌传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('6e7fd21958c94e21ae6a8fa00d4d4fcc', '璩红', '14568005329', 'chenglei@min.cn', '2018-11-21 09:01:57.383287', '2018-11-21 09:01:57.383287', '银嘉科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('74fad7f2f5d54b219f49aad7998815f4', '伯雷', '15581941224', 'weiqiao@lailuo.cn', '2018-11-21 09:01:56.207627', '2018-11-21 09:01:56.207627', '商软冠联科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('77523e4ae0334f31bf819c946edf2d8e', '邱静', '15588092702', 'chaolin@gmail.com', '2018-11-21 09:01:57.033188', '2018-11-21 09:01:57.033188', '天益信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('79517fa955b6486785105bafd4860a2c', '梁玉梅', '18846786133', 'wcui@82.cn', '2018-11-21 09:01:57.482985', '2018-11-21 09:01:57.482985', '良诺科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('8472b1ec03e64a09a63e23b9d7136f73', '仇桂芳', '18832315833', 'jinchao@feng.cn', '2018-11-21 09:01:57.360312', '2018-11-21 09:01:57.360312', '网新恒天科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('8527c1a0c614419e9cc51e7219fe3e7a', '鲁玉梅', '15673417549', 'pingzou@leiwei.cn', '2018-11-21 09:01:55.399770', '2018-11-21 09:01:55.399770', '诺依曼软件传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('85a9694447ef4b35b0338f6ba7601270', '夔玉', '13043008427', 'chaogao@qianglei.cn', '2018-11-21 09:01:56.552733', '2018-11-21 09:01:56.552733', '盟新科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('887677767a0b4e54b42384d30214e724', '段玉英', '18857234110', 'lei29@li.cn', '2018-11-21 09:01:56.782774', '2018-11-21 09:01:56.782774', '恒聪百汇传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('8aacd5462e8b4f3a9fe7cebfef1506c9', '墨强', '15248099884', 'qyi@yahoo.com', '2018-11-21 09:01:56.960382', '2018-11-21 09:01:56.960382', '泰麒麟网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('8c725b30d20d424ca611308e0da8aa79', '纪俊', '15219677850', 'weijie@yan.cn', '2018-11-21 09:01:57.110510', '2018-11-21 09:01:57.110510', '银嘉网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('8cd061e34be54fa19e39502b475413a9', '裘莉', '13438354392', 'gangxiang@yahoo.com', '2018-11-21 09:01:55.294050', '2018-11-21 09:01:55.294050', '巨奥传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('8e09088c51bb40bb88dc08165ac15fbd', '冉丽华', '13348699258', 'luoyong@yahoo.com', '2018-11-21 09:01:57.833046', '2018-11-21 09:01:57.833046', '南康传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('91a2dc2e7c98427fbcc3429a568e6880', '黎帅', '13369246644', 'tanyang@gmail.com', '2018-11-21 09:01:56.983379', '2018-11-21 09:01:56.983379', '同兴万点网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('91ad0cd87e00497ba3d65ba418150cd5', '羊桂英', '15096412805', 'shenchao@daili.cn', '2018-11-21 09:01:57.282523', '2018-11-21 09:01:57.282523', '开发区世创科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('9368ade53af8441e93cc54779b8182cd', '乐秀荣', '13655462210', 'stao@jin.cn', '2018-11-21 09:01:56.702968', '2018-11-21 09:01:56.702968', '太极科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('947e0e4e237c465eade7165159e7c7f1', '万兵', '13474049918', 'songyang@gmail.com', '2018-11-21 09:01:57.933765', '2018-11-21 09:01:57.934271', '创汇传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('94c27c9f3769417f88cd46b99a76ccd2', '全桂荣', '18041520321', 'jingcui@hotmail.com', '2018-11-21 09:01:57.683181', '2018-11-21 09:01:57.683181', '维旺明传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('991739c8a24445b688e03e8b3671d6b1', '汪凯', '13940379984', 'bfan@yanzou.cn', '2018-11-21 09:01:58.693192', '2018-11-21 09:01:58.693192', '天开科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('9c6bbe3c200b41519188261f509cd67d', '莘红梅', '13367733143', 'ycheng@chaotao.cn', '2018-11-21 09:01:55.327964', '2018-11-21 09:01:55.327964', '华泰通安科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('a32ed966afdf47349425d23c6f8bb170', '巫建军', '15709656023', 'guiyingkong@weigang.cn', '2018-11-21 09:01:57.333212', '2018-11-21 09:01:57.333383', '华泰通安传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('a39395f9abde44f889a70179401424b8', '慕俊', '14760036796', 'yuanjing@gmail.com', '2018-11-21 09:01:58.591380', '2018-11-21 09:01:58.591380', '雨林木风计算机科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('a424f953d0ee434e9d2fcd6e773bd36e', '后桂芳', '15836865796', 'luochao@mojin.cn', '2018-11-21 09:01:57.312438', '2018-11-21 09:01:57.312438', 'MBP软件信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('a4b9a7f3f99b4705a01a1df718e7ed2d', '牧凤兰', '15020770631', 'xia97@yong.org', '2018-11-21 09:01:57.061116', '2018-11-21 09:01:57.061116', '良诺传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('a530ffa4192d454cb28a7b1f332df6be', '璩凯', '18168759433', 'yan96@gmail.com', '2018-11-21 09:01:57.960476', '2018-11-21 09:01:57.960476', '昊嘉信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('a84477e715904f30aa7267230000ea3d', '彭莹', '13789915832', 'tliang@62.org', '2018-11-21 09:01:56.511077', '2018-11-21 09:01:56.511077', '银嘉网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('ac17533273e54c91bfec90e36ba38610', '郭利', '18570420600', 'longjun@ew.cn', '2018-11-21 09:01:56.733886', '2018-11-21 09:01:56.733935', '超艺信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('ac5ec876f71b463e95ea5fb8fdcd9fec', '雕娟', '13831260070', 'xia52@li.com', '2018-11-21 09:01:57.910827', '2018-11-21 09:01:57.910827', '毕博诚网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('ad65752ce93248489f5d49a10c7ffce5', '红建', '13596015750', 'gangxu@14.net', '2018-11-21 09:01:56.911103', '2018-11-21 09:01:56.911103', '毕博诚网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('b1bb24afb1b144a381cf401b88c62c5e', '刘志强', '13927192487', 'dpeng@weijun.cn', '2018-11-21 09:01:57.432339', '2018-11-21 09:01:57.432339', '中建创业传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('b2963e741a44417bb23340ecf48e67c4', '申想', '18800031221', 'gang95@dq.cn', '2018-11-21 09:01:57.760248', '2018-11-21 09:01:57.760248', '合联电子信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('befb8c99c49445d79870536496637da5', '杜冬梅', '15257672350', 'wei66@hotmail.com', '2018-11-21 09:01:56.257472', '2018-11-21 09:01:56.257472', '方正科技科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('bf07dbcf80d947749c781ed9d72fdbbf', '霍勇', '13926281048', 'tanjuan@ding.cn', '2018-11-21 09:01:58.232444', '2018-11-21 09:01:58.232444', '立信电子科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('c5c33727c7784ea4a82466e715ca4b7c', '鄂伟', '15387426593', 'pren@gmail.com', '2018-11-21 09:01:58.519676', '2018-11-21 09:01:58.519676', '鸿睿思博科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('c9b3701562914e18a937cb64d57503e0', '帅建', '18257957284', 'nayu@hotmail.com', '2018-11-21 09:01:58.569668', '2018-11-21 09:01:58.569668', '毕博诚传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('cb7b89cf6b924f419f622eff9eb45335', '昌淑华', '14725521571', 'zouqiang@yicai.cn', '2018-11-21 09:01:57.811108', '2018-11-21 09:01:57.811108', '明腾科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('cd2d70f03e9f44169b0f35d49b43501a', '劳秀云', '15561245270', 'nadai@yahoo.com', '2018-11-21 09:01:58.010651', '2018-11-21 09:01:58.010651', '时空盒数字传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('cd2f94e4de84451d8646cab7a91c4094', '向帆', '15760910946', 'hxu@hotmail.com', '2018-11-21 09:01:58.440886', '2018-11-21 09:01:58.440886', '商软冠联传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('cdb156f31cbf4b6a8edc835abfc52f79', '屈丹', '15710705630', 'xiulan84@yanchang.com', '2018-11-21 09:01:55.427755', '2018-11-21 09:01:55.427755', '戴硕电子网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('d105fa5b8fe74760b1f9293a3945d52e', '束坤', '15323504093', 'lwen@fangwu.cn', '2018-11-21 09:01:56.652712', '2018-11-21 09:01:56.652712', '易动力科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('d3a9dd48fbcc4bd681eb7dc4795f9e60', '荆磊', '18684741753', 'luna@jh.cn', '2018-11-21 09:01:55.349901', '2018-11-21 09:01:55.349901', '华远软件网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('d401090228fd4ad2952160bbb700cf4d', '倪涛', '18882169324', 'gangwan@yahoo.com', '2018-11-21 09:01:57.210712', '2018-11-21 09:01:57.210712', '和泰传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('d4d89749185f424b87b048245c9e092a', '厉成', '15232534957', 'scao@shiguo.cn', '2018-11-21 09:01:56.760847', '2018-11-21 09:01:56.760847', '菊风公司传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('dc1ac80387964b4d915d4d6b1539cfd7', '闵宇', '15131540328', 'dlu@ming.cn', '2018-11-21 09:01:58.669220', '2018-11-21 09:01:58.669220', '和泰科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('dd6dbd7271c24baab5d64dbe918ff0da', '却斌', '15086044482', 'fang48@hotmail.com', '2018-11-21 09:01:58.361099', '2018-11-21 09:01:58.361099', '惠派国际公司传媒有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('df9a545dab364e85bf2f0ca3a332d28c', '仲杨', '15300054855', 'xiajing@gmail.com', '2018-11-21 09:01:57.660508', '2018-11-21 09:01:57.660508', '思优网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('e14144f165074275a8e29a2e08b70245', '薛燕', '13783047602', 'yongtang@weiyin.cn', '2018-11-21 09:01:58.088887', '2018-11-21 09:01:58.088887', '精芯信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('e3f5726479194294b8414b5b88e1fa9c', '祝玉华', '13015407546', 'wei18@hotmail.com', '2018-11-21 09:01:57.182786', '2018-11-21 09:01:57.182786', '昊嘉信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('e56e0e84fbac4fe6aaa7eb1acb33eaf2', '太超', '15241318421', 'qiang55@hotmail.com', '2018-11-21 09:01:58.769996', '2018-11-21 09:01:58.769996', '开发区世创网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('ebcccff23d354d0dbb2e29bdef518f4a', '公刚', '13942916391', 'changmin@hotmail.com', '2018-11-21 09:01:57.086043', '2018-11-21 09:01:57.086043', '恒聪百汇科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('ed71aca747bb42c2a8b269e686e5026f', '都明', '15738450771', 'minyu@hotmail.com', '2018-11-21 09:01:58.125726', '2018-11-21 09:01:58.125726', '超艺科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('ef41ebea28f24093b9cc2175f25d3480', '陶勇', '18100517509', 'lei83@yahoo.com', '2018-11-21 09:01:56.601847', '2018-11-21 09:01:56.601847', '太极信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('efbb763f580c4fcfac24314eeb79d88c', '西小红', '18066193807', 'vtang@leiliang.cn', '2018-11-21 09:01:57.883911', '2018-11-21 09:01:57.883911', '昊嘉科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('f0fc22132ff14387b3b13cdde9c6fcc8', '须丹丹', '14552139326', 'xiaojie@gmail.com', '2018-11-21 09:01:56.675044', '2018-11-21 09:01:56.675044', '银嘉信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('f1723e7293984c478eb18959f43abc15', '殳红', '15681837167', 'chao19@ming.cn', '2018-11-21 09:01:57.783187', '2018-11-21 09:01:57.783187', '四通信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('f414bff1bc0c4422ad616253aa1746ce', '空慧', '18877007493', 'leima@hotmail.com', '2018-11-21 09:01:57.710380', '2018-11-21 09:01:57.710380', '惠派国际公司科技有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('f815121a2b12470094a2d5947c924dff', '南玉珍', '13719203056', 'ghe@gmail.com', '2018-11-21 09:01:56.933355', '2018-11-21 09:01:56.933355', '海创网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('f904ccb181044375a4848aa3ef7f0249', '许桂芝', '15193906758', 'qyan@hotmail.com', '2018-11-21 09:01:57.582721', '2018-11-21 09:01:57.582721', '明腾信息有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('ff5f3f3899bc487b870dfc33c0f7a555', '翟楠', '15668940449', 'chaoliang@gr.net', '2018-11-21 09:01:57.260577', '2018-11-21 09:01:57.260577', '创联世纪网络有限公司', 'photos/default_user.jpg');
INSERT INTO `study_user` VALUES ('ff6b26fa53854165a050a896ae9647bd', '莘欢', '13788136279', 'xiangna@07.cn', '2018-11-21 09:01:58.173025', '2018-11-21 09:01:58.173025', '时空盒数字科技有限公司', 'photos/default_user.jpg');

SET FOREIGN_KEY_CHECKS = 1;
