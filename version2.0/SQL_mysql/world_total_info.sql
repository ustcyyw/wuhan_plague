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

 Date: 19/02/2020 22:53:36
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for world_total_info
-- ----------------------------
DROP TABLE IF EXISTS `world_total_info`;
CREATE TABLE `world_total_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `diagnosis_num` int(11) NOT NULL COMMENT '确诊人数',
  `suspect_num` int(11) NOT NULL COMMENT '疑似人数',
  `cure_num` int(11) NOT NULL COMMENT '治愈人数',
  `death_num` int(11) NOT NULL COMMENT '死亡人数',
  `recording_time` timestamp(0) NOT NULL ON UPDATE CURRENT_TIMESTAMP(0) COMMENT '记录时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 683 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of world_total_info
-- ----------------------------
INSERT INTO `world_total_info` VALUES (630, 698, 0, 109, 3, '2020-02-17 16:09:35');
INSERT INTO `world_total_info` VALUES (631, 797, 0, 109, 3, '2020-02-17 17:09:42');
INSERT INTO `world_total_info` VALUES (632, 797, 0, 109, 3, '2020-02-17 18:09:49');