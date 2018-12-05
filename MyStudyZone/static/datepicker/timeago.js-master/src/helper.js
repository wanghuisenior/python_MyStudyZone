/**
 * Created by hustcc on 18/5/20.
 * Contract: i@hust.cc
 */

import { SEC_ARRAY, ATTR_DATA_TID, ATTR_TIMEAGO, ATTR_DATETIME } from './constant';
import { Locales } from './locales';

/**
 * change f into int, remove decimal. Just for code compression
 * @param f
 * @returns {number}
 */
export const toInt = f => parseInt(f);

/**
 * format Date / string / timestamp to Date instance.
 * @param input
 * @returns {*}
 */
export const toDate = input => {
  if (input instanceof Date) return input;
  if (!isNaN(input) || /^\d+$/.test(input)) return new Date(toInt(input));
  input = (input || '').trim().replace(/\.\d+/, '') // remove milliseconds
    .replace(/-/, '/').replace(/-/, '/')
    .replace(/(\d)T(\d)/, '$1 $2').replace(/Z/, ' UTC') // 2017-2-5T3:57:52Z -> 2017-2-5 3:57:52UTC
    .replace(/([\+\-]\d\d)\:?(\d\d)/, ' $1$2'); // -04:00 -> -0400
  return new Date(input);
};

/**
 * format the diff second to *** time ago, with setting locale
 * @param diff
 * @param locale
 * @param defaultLocale
 * @returns {string | void | *}
 */
export const formatDiff = (diff, locale, defaultLocale) => {
  // if locale is not exist, use defaultLocale.
  // if defaultLocale is not exist, use build-in `en`.
  // be sure of no error when locale is not exist.
  locale = Locales[locale] ? locale : (Locales[defaultLocale] ? defaultLocale : 'en');
  let i = 0,
    agoin = diff < 0 ? 1 : 0, // timein or timeago
    total_sec = diff = Math.abs(diff);

  for (; diff >= SEC_ARRAY[i] && i < SEC_ARRAY.length; i++) {
    diff /= SEC_ARRAY[i];
  }
  diff = toInt(diff);
  i *= 2;

  if (diff > (i === 0 ? 9 : 1)) i += 1;
  return Locales[locale](diff, i, total_sec)[agoin].replace('%s', diff);
};

/**
 * calculate the diff second between date to be formatted an now date.
 * @param date
 * @param nowDate
 * @returns {number}
 */
export const diffSec = (date, nowDate) => {
  nowDate = nowDate ? toDate(nowDate) : new Date();
  return (nowDate - toDate(date)) / 1000;
};

/**
 * nextInterval: calculate the next interval time.
 * - diff: the diff sec between now and date to be formatted.
 *
 * What's the meaning?
 * diff = 61 then return 59
 * diff = 3601 (an hour + 1 second), then return 3599
 * make the interval with high performance.
 **/
export const nextInterval = diff => {
  let rst = 1, i = 0, d = Math.abs(diff);
  for (; diff >= SEC_ARRAY[i] && i < SEC_ARRAY.length; i ++) {
    diff /= SEC_ARRAY[i];
    rst *= SEC_ARRAY[i];
  }
  d = d % rst;
  d = d ? rst - d : rst;
  return Math.ceil(d);
};

/**
 * get the node attribute, native DOM and jquery supported.
 * @param node
 * @param name
 * @returns {*}
 */
export const getAttr = (node, name) => {
  if (node.getAttribute) return node.getAttribute(name); // native dom
  if (node.attr) return node.attr(name); // jquery dom
};

/**
 * get the datetime attribute, `data-timeagp` / `datetime` are supported.
 * @param node
 * @returns {*}
 */
export const getDateAttr = node => getAttr(node, ATTR_TIMEAGO) || getAttr(node, ATTR_DATETIME);

/**
 * set the node attribute, native DOM and jquery supported.
 * @param node
 * @param val
 * @returns {*}
 */
export const setTidAttr = (node, val) => {
  if (node.setAttribute) return node.setAttribute(ATTR_DATA_TID, val);
  if (node.attr) return node.attr(ATTR_DATA_TID, val);
};
