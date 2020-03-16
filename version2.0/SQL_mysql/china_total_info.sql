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

 Date: 19/02/2020 22:53:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for china_total_info
-- ----------------------------
DROP TABLE IF EXISTS `china_total_info`;
CREATE TABLE `china_total_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `diagnosis_num` int(11) NOT NULL COMMENT '确诊人数',
  `suspect_num` int(11) NOT NULL COMMENT '疑似人数',
  `cure_num` int(11) NOT NULL COMMENT '治愈人数',
  `death_num` int(11) NOT NULL COMMENT '死亡人数',
  `recording_time` timestamp(0) NOT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '记录时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 685 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of china_total_info
-- ----------------------------
INSERT INTO `china_total_info` VALUES (12, 321, 162, 25, 6, '2020-01-22 00:53:20');
INSERT INTO `china_total_info` VALUES (13, 321, 163, 25, 6, '2020-01-22 01:53:26');
INSERT INTO `china_total_info` VALUES (14, 321, 163, 25, 6, '2020-01-22 02:53:30');
INSERT INTO `china_total_info` VALUES (15, 321, 163, 25, 6, '2020-01-22 03:53:34');