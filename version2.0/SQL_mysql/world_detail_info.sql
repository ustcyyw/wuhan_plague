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

 Date: 19/02/2020 22:53:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for world_detail_info
-- ----------------------------
DROP TABLE IF EXISTS `world_detail_info`;
CREATE TABLE `world_detail_info`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `count` int(11) NOT NULL COMMENT '表示这是第几次记录',
  `province` varchar(255) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL COMMENT '省级区划名字',
  `diagnosis_num` int(11) NOT NULL,
  `suspect_num` int(11) NOT NULL,
  `cure_num` int(11) NOT NULL,
  `death_num` int(11) NOT NULL,
  `recording_time` timestamp(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21036 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of world_detail_info
-- ----------------------------
INSERT INTO `world_detail_info` VALUES (19606, 1, '钻石公主号邮轮', 355, 0, 0, 0, '2020-02-17 16:09:32');
INSERT INTO `world_detail_info` VALUES (19607, 1, '新加坡', 75, 0, 19, 0, '2020-02-17 16:09:32');
INSERT INTO `world_detail_info` VALUES (19608, 1, '日本', 62, 0, 12, 1, '2020-02-17 16:09:32');