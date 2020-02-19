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
INSERT INTO `world_total_info` VALUES (633, 797, 0, 109, 3, '2020-02-17 19:09:55');
INSERT INTO `world_total_info` VALUES (634, 797, 0, 109, 3, '2020-02-17 20:10:01');
INSERT INTO `world_total_info` VALUES (635, 797, 0, 109, 3, '2020-02-17 21:10:07');
INSERT INTO `world_total_info` VALUES (636, 797, 0, 109, 3, '2020-02-17 22:10:12');
INSERT INTO `world_total_info` VALUES (637, 799, 0, 114, 3, '2020-02-17 23:10:19');
INSERT INTO `world_total_info` VALUES (638, 800, 0, 114, 3, '2020-02-18 00:10:25');
INSERT INTO `world_total_info` VALUES (639, 800, 0, 114, 3, '2020-02-18 01:10:32');
INSERT INTO `world_total_info` VALUES (640, 800, 0, 114, 3, '2020-02-18 02:10:39');
INSERT INTO `world_total_info` VALUES (641, 800, 0, 114, 3, '2020-02-18 03:10:45');
INSERT INTO `world_total_info` VALUES (642, 800, 0, 114, 3, '2020-02-18 04:10:51');
INSERT INTO `world_total_info` VALUES (643, 800, 0, 114, 3, '2020-02-18 05:10:57');
INSERT INTO `world_total_info` VALUES (644, 800, 0, 114, 3, '2020-02-18 06:11:03');
INSERT INTO `world_total_info` VALUES (645, 800, 0, 114, 3, '2020-02-18 07:11:10');
INSERT INTO `world_total_info` VALUES (646, 800, 0, 116, 3, '2020-02-18 08:11:16');
INSERT INTO `world_total_info` VALUES (647, 800, 0, 116, 3, '2020-02-18 09:11:22');
INSERT INTO `world_total_info` VALUES (648, 800, 0, 116, 3, '2020-02-18 10:11:29');
INSERT INTO `world_total_info` VALUES (649, 800, 0, 116, 3, '2020-02-18 11:11:35');
INSERT INTO `world_total_info` VALUES (650, 800, 0, 116, 3, '2020-02-18 12:11:42');
INSERT INTO `world_total_info` VALUES (651, 800, 0, 116, 3, '2020-02-18 13:11:48');
INSERT INTO `world_total_info` VALUES (652, 800, 0, 116, 3, '2020-02-18 14:11:55');
INSERT INTO `world_total_info` VALUES (653, 800, 0, 116, 3, '2020-02-18 15:12:01');
INSERT INTO `world_total_info` VALUES (654, 800, 0, 116, 3, '2020-02-18 16:12:08');
INSERT INTO `world_total_info` VALUES (655, 800, 0, 116, 3, '2020-02-18 17:12:14');
INSERT INTO `world_total_info` VALUES (656, 888, 0, 116, 3, '2020-02-18 18:12:20');
INSERT INTO `world_total_info` VALUES (657, 888, 0, 116, 3, '2020-02-18 19:12:26');
INSERT INTO `world_total_info` VALUES (658, 888, 0, 116, 3, '2020-02-18 20:12:33');
INSERT INTO `world_total_info` VALUES (659, 888, 0, 116, 3, '2020-02-18 21:12:43');
INSERT INTO `world_total_info` VALUES (660, 888, 0, 116, 3, '2020-02-18 22:12:50');
INSERT INTO `world_total_info` VALUES (661, 900, 0, 118, 3, '2020-02-18 23:12:56');
INSERT INTO `world_total_info` VALUES (662, 900, 0, 118, 3, '2020-02-19 00:13:04');
INSERT INTO `world_total_info` VALUES (663, 900, 0, 124, 3, '2020-02-19 01:13:10');
INSERT INTO `world_total_info` VALUES (664, 900, 0, 124, 3, '2020-02-19 02:13:17');
INSERT INTO `world_total_info` VALUES (665, 900, 0, 124, 3, '2020-02-19 03:13:24');
INSERT INTO `world_total_info` VALUES (666, 900, 0, 124, 3, '2020-02-19 04:13:30');
INSERT INTO `world_total_info` VALUES (667, 900, 0, 124, 3, '2020-02-19 05:13:36');
INSERT INTO `world_total_info` VALUES (668, 900, 0, 124, 3, '2020-02-19 06:13:42');
INSERT INTO `world_total_info` VALUES (669, 900, 0, 124, 3, '2020-02-19 07:13:48');
INSERT INTO `world_total_info` VALUES (670, 900, 0, 124, 3, '2020-02-19 08:13:54');
INSERT INTO `world_total_info` VALUES (671, 900, 0, 124, 3, '2020-02-19 09:13:59');
INSERT INTO `world_total_info` VALUES (672, 920, 0, 129, 3, '2020-02-19 10:14:07');
INSERT INTO `world_total_info` VALUES (673, 920, 0, 129, 3, '2020-02-19 11:14:13');
INSERT INTO `world_total_info` VALUES (674, 920, 0, 129, 3, '2020-02-19 12:14:18');
INSERT INTO `world_total_info` VALUES (675, 920, 0, 129, 3, '2020-02-19 13:14:24');
INSERT INTO `world_total_info` VALUES (676, 920, 0, 129, 3, '2020-02-19 14:14:30');
INSERT INTO `world_total_info` VALUES (677, 920, 0, 133, 3, '2020-02-19 15:14:37');
INSERT INTO `world_total_info` VALUES (678, 920, 0, 133, 3, '2020-02-19 16:14:42');
INSERT INTO `world_total_info` VALUES (679, 920, 0, 133, 3, '2020-02-19 17:14:48');
INSERT INTO `world_total_info` VALUES (680, 925, 0, 135, 3, '2020-02-19 18:14:54');
INSERT INTO `world_total_info` VALUES (681, 925, 0, 135, 3, '2020-02-19 19:15:00');
INSERT INTO `world_total_info` VALUES (682, 925, 0, 135, 3, '2020-02-19 20:15:07');
INSERT INTO `world_total_info` VALUES (683, 1007, 0, 140, 3, '2020-02-19 21:15:12');
INSERT INTO `world_total_info` VALUES (684, 1017, 0, 144, 3, '2020-02-19 22:15:19');

SET FOREIGN_KEY_CHECKS = 1;
