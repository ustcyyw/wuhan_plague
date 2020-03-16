/*
 Navicat Premium Data Transfer

 Source Server         : yyw
 Source Server Type    : MySQL
 Source Server Version : 80016
 Source Host           : localhost:3306
 Source Schema         : plague_info

 Target Server Type    : MySQL
 Target Server Version : 80016
 File Encoding         : 65001

 Date: 19/02/2020 22:52:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for china_detail_info
-- ----------------------------
DROP TABLE IF EXISTS `china_detail_info`;
CREATE TABLE `china_detail_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `count` int(11) NOT NULL COMMENT '表示这是第几次记录',
  `province` varchar(255) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL COMMENT '省级区划名字',
  `diagnosis_num` int(11) NOT NULL,
  `suspect_num` int(11) NOT NULL,
  `cure_num` int(11) NOT NULL,
  `death_num` int(11) NOT NULL,
  `recording_time` timestamp(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21510 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of china_detail_info
-- ----------------------------
INSERT INTO `china_detail_info` VALUES (111, 1, '湖北', 270, 11, 25, 6, '2020-01-22 00:53:20');
INSERT INTO `china_detail_info` VALUES (112, 1, '北京', 10, 0, 0, 0, '2020-01-22 00:53:21');
INSERT INTO `china_detail_info` VALUES (113, 1, '广东', 17, 4, 0, 0, '2020-01-22 00:53:21');