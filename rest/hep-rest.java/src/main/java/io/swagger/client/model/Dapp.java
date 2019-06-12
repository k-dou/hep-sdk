/*
 * HEP REST API
 * The REST API for HEP protocol
 *
 * OpenAPI spec version: v1
 * Contact: xiawu@zeuux.org
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.swagger.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * Dapp
 */

@javax.annotation.Generated(value = "io.swagger.codegen.v3.generators.java.JavaClientCodegen", date = "2019-06-12T11:49:49.487+08:00[Asia/Shanghai]")public class Dapp {

  @SerializedName("dapp_key")
  private String dappKey = null;

  @SerializedName("protocol")
  private String protocol = null;

  @SerializedName("version")
  private String version = null;

  @SerializedName("ts")
  private Integer ts = null;

  @SerializedName("nonce")
  private String nonce = null;

  @SerializedName("os")
  private String os = null;

  @SerializedName("language")
  private String language = null;

  @SerializedName("md5")
  private String md5 = null;

  @SerializedName("dapp_id")
  private String dappId = null;

  @SerializedName("dapp_name")
  private String dappName = null;

  @SerializedName("icon")
  private String icon = null;

  @SerializedName("public_key")
  private String publicKey = null;

  @SerializedName("package_name")
  private String packageName = null;

  @SerializedName("bundle_id")
  private String bundleId = null;

  @SerializedName("schema")
  private String schema = null;

  @SerializedName("website")
  private String website = null;

  @SerializedName("download_url")
  private String downloadUrl = null;

  @SerializedName("deposit_contract_address")
  private String depositContractAddress = null;

  @SerializedName("dapp_type")
  private String dappType = null;

  @SerializedName("dapp_category")
  private String dappCategory = null;

  @SerializedName("auth_login_callback")
  private String authLoginCallback = null;

  @SerializedName("pay_order_callback")
  private String payOrderCallback = null;

  @SerializedName("proof_submit_callback")
  private String proofSubmitCallback = null;
  public Dapp dappKey(String dappKey) {
    this.dappKey = dappKey;
    return this;
  }

  

  /**
  * The decentralized application access key
  * @return dappKey
  **/
  @Schema(required = true, description = "The decentralized application access key")
  public String getDappKey() {
    return dappKey;
  }
  public void setDappKey(String dappKey) {
    this.dappKey = dappKey;
  }
  public Dapp protocol(String protocol) {
    this.protocol = protocol;
    return this;
  }

  

  /**
  * The protocol name. default is &#x27;HEP&#x27;.
  * @return protocol
  **/
  @Schema(required = true, description = "The protocol name. default is 'HEP'.")
  public String getProtocol() {
    return protocol;
  }
  public void setProtocol(String protocol) {
    this.protocol = protocol;
  }
  public Dapp version(String version) {
    this.version = version;
    return this;
  }

  

  /**
  * The protocol version such as &#x27;1.0&#x27;
  * @return version
  **/
  @Schema(required = true, description = "The protocol version such as '1.0'")
  public String getVersion() {
    return version;
  }
  public void setVersion(String version) {
    this.version = version;
  }
  public Dapp ts(Integer ts) {
    this.ts = ts;
    return this;
  }

  

  /**
  * The current timestamp
  * @return ts
  **/
  @Schema(required = true, description = "The current timestamp")
  public Integer getTs() {
    return ts;
  }
  public void setTs(Integer ts) {
    this.ts = ts;
  }
  public Dapp nonce(String nonce) {
    this.nonce = nonce;
    return this;
  }

  

  /**
  * The random string or auto-increment sequence
  * @return nonce
  **/
  @Schema(required = true, description = "The random string or auto-increment sequence")
  public String getNonce() {
    return nonce;
  }
  public void setNonce(String nonce) {
    this.nonce = nonce;
  }
  public Dapp os(String os) {
    this.os = os;
    return this;
  }

  

  /**
  * The operating system of client such as ios, android, dweb,etc.
  * @return os
  **/
  @Schema(required = true, description = "The operating system of client such as ios, android, dweb,etc.")
  public String getOs() {
    return os;
  }
  public void setOs(String os) {
    this.os = os;
  }
  public Dapp language(String language) {
    this.language = language;
    return this;
  }

  

  /**
  * The i18n language code such as zh, en, etc.
  * @return language
  **/
  @Schema(required = true, description = "The i18n language code such as zh, en, etc.")
  public String getLanguage() {
    return language;
  }
  public void setLanguage(String language) {
    this.language = language;
  }
  public Dapp md5(String md5) {
    this.md5 = md5;
    return this;
  }

  

  /**
  * The HMAC authentication md5 checksum
  * @return md5
  **/
  @Schema(required = true, description = "The HMAC authentication md5 checksum")
  public String getMd5() {
    return md5;
  }
  public void setMd5(String md5) {
    this.md5 = md5;
  }
  public Dapp dappId(String dappId) {
    this.dappId = dappId;
    return this;
  }

  

  /**
  * The decentralized application ID
  * @return dappId
  **/
  @Schema(required = true, description = "The decentralized application ID")
  public String getDappId() {
    return dappId;
  }
  public void setDappId(String dappId) {
    this.dappId = dappId;
  }
  public Dapp dappName(String dappName) {
    this.dappName = dappName;
    return this;
  }

  

  /**
  * The decentralized application name
  * @return dappName
  **/
  @Schema(required = true, description = "The decentralized application name")
  public String getDappName() {
    return dappName;
  }
  public void setDappName(String dappName) {
    this.dappName = dappName;
  }
  public Dapp icon(String icon) {
    this.icon = icon;
    return this;
  }

  

  /**
  * The icon of application
  * @return icon
  **/
  @Schema(required = true, description = "The icon of application")
  public String getIcon() {
    return icon;
  }
  public void setIcon(String icon) {
    this.icon = icon;
  }
  public Dapp publicKey(String publicKey) {
    this.publicKey = publicKey;
    return this;
  }

  

  /**
  * The public key of DApp
  * @return publicKey
  **/
  @Schema(required = true, description = "The public key of DApp")
  public String getPublicKey() {
    return publicKey;
  }
  public void setPublicKey(String publicKey) {
    this.publicKey = publicKey;
  }
  public Dapp packageName(String packageName) {
    this.packageName = packageName;
    return this;
  }

  

  /**
  * The package name such as com.demo.dev.android
  * @return packageName
  **/
  @Schema(required = true, description = "The package name such as com.demo.dev.android")
  public String getPackageName() {
    return packageName;
  }
  public void setPackageName(String packageName) {
    this.packageName = packageName;
  }
  public Dapp bundleId(String bundleId) {
    this.bundleId = bundleId;
    return this;
  }

  

  /**
  * The bundle id such as com.demo.dev.ios for iOS platform
  * @return bundleId
  **/
  @Schema(required = true, description = "The bundle id such as com.demo.dev.ios for iOS platform")
  public String getBundleId() {
    return bundleId;
  }
  public void setBundleId(String bundleId) {
    this.bundleId = bundleId;
  }
  public Dapp schema(String schema) {
    this.schema = schema;
    return this;
  }

  

  /**
  * The routing schema
  * @return schema
  **/
  @Schema(required = true, description = "The routing schema")
  public String getSchema() {
    return schema;
  }
  public void setSchema(String schema) {
    this.schema = schema;
  }
  public Dapp website(String website) {
    this.website = website;
    return this;
  }

  

  /**
  * The dapp website link
  * @return website
  **/
  @Schema(required = true, description = "The dapp website link")
  public String getWebsite() {
    return website;
  }
  public void setWebsite(String website) {
    this.website = website;
  }
  public Dapp downloadUrl(String downloadUrl) {
    this.downloadUrl = downloadUrl;
    return this;
  }

  

  /**
  * The dapp download link
  * @return downloadUrl
  **/
  @Schema(required = true, description = "The dapp download link")
  public String getDownloadUrl() {
    return downloadUrl;
  }
  public void setDownloadUrl(String downloadUrl) {
    this.downloadUrl = downloadUrl;
  }
  public Dapp depositContractAddress(String depositContractAddress) {
    this.depositContractAddress = depositContractAddress;
    return this;
  }

  

  /**
  * The deposit contract Address, the example is NEW182....
  * @return depositContractAddress
  **/
  @Schema(required = true, description = "The deposit contract Address, the example is NEW182....")
  public String getDepositContractAddress() {
    return depositContractAddress;
  }
  public void setDepositContractAddress(String depositContractAddress) {
    this.depositContractAddress = depositContractAddress;
  }
  public Dapp dappType(String dappType) {
    this.dappType = dappType;
    return this;
  }

  

  /**
  * The dapp type. choices:android, ios, dweb,newdapp.
  * @return dappType
  **/
  @Schema(required = true, description = "The dapp type. choices:android, ios, dweb,newdapp.")
  public String getDappType() {
    return dappType;
  }
  public void setDappType(String dappType) {
    this.dappType = dappType;
  }
  public Dapp dappCategory(String dappCategory) {
    this.dappCategory = dappCategory;
    return this;
  }

  

  /**
  * The dapp category. choices: game, retail.
  * @return dappCategory
  **/
  @Schema(required = true, description = "The dapp category. choices: game, retail.")
  public String getDappCategory() {
    return dappCategory;
  }
  public void setDappCategory(String dappCategory) {
    this.dappCategory = dappCategory;
  }
  public Dapp authLoginCallback(String authLoginCallback) {
    this.authLoginCallback = authLoginCallback;
    return this;
  }

  

  /**
  * For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.
  * @return authLoginCallback
  **/
  @Schema(required = true, description = "For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.")
  public String getAuthLoginCallback() {
    return authLoginCallback;
  }
  public void setAuthLoginCallback(String authLoginCallback) {
    this.authLoginCallback = authLoginCallback;
  }
  public Dapp payOrderCallback(String payOrderCallback) {
    this.payOrderCallback = payOrderCallback;
    return this;
  }

  

  /**
  * For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.
  * @return payOrderCallback
  **/
  @Schema(required = true, description = "For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.")
  public String getPayOrderCallback() {
    return payOrderCallback;
  }
  public void setPayOrderCallback(String payOrderCallback) {
    this.payOrderCallback = payOrderCallback;
  }
  public Dapp proofSubmitCallback(String proofSubmitCallback) {
    this.proofSubmitCallback = proofSubmitCallback;
    return this;
  }

  

  /**
  * For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.
  * @return proofSubmitCallback
  **/
  @Schema(required = true, description = "For Mobile Native DApp, it is redirect schema; For website DApp, it is callback url; For  NewDApp, it is HEP-based url.")
  public String getProofSubmitCallback() {
    return proofSubmitCallback;
  }
  public void setProofSubmitCallback(String proofSubmitCallback) {
    this.proofSubmitCallback = proofSubmitCallback;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Dapp dapp = (Dapp) o;
    return Objects.equals(this.dappKey, dapp.dappKey) &&
        Objects.equals(this.protocol, dapp.protocol) &&
        Objects.equals(this.version, dapp.version) &&
        Objects.equals(this.ts, dapp.ts) &&
        Objects.equals(this.nonce, dapp.nonce) &&
        Objects.equals(this.os, dapp.os) &&
        Objects.equals(this.language, dapp.language) &&
        Objects.equals(this.md5, dapp.md5) &&
        Objects.equals(this.dappId, dapp.dappId) &&
        Objects.equals(this.dappName, dapp.dappName) &&
        Objects.equals(this.icon, dapp.icon) &&
        Objects.equals(this.publicKey, dapp.publicKey) &&
        Objects.equals(this.packageName, dapp.packageName) &&
        Objects.equals(this.bundleId, dapp.bundleId) &&
        Objects.equals(this.schema, dapp.schema) &&
        Objects.equals(this.website, dapp.website) &&
        Objects.equals(this.downloadUrl, dapp.downloadUrl) &&
        Objects.equals(this.depositContractAddress, dapp.depositContractAddress) &&
        Objects.equals(this.dappType, dapp.dappType) &&
        Objects.equals(this.dappCategory, dapp.dappCategory) &&
        Objects.equals(this.authLoginCallback, dapp.authLoginCallback) &&
        Objects.equals(this.payOrderCallback, dapp.payOrderCallback) &&
        Objects.equals(this.proofSubmitCallback, dapp.proofSubmitCallback);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(dappKey, protocol, version, ts, nonce, os, language, md5, dappId, dappName, icon, publicKey, packageName, bundleId, schema, website, downloadUrl, depositContractAddress, dappType, dappCategory, authLoginCallback, payOrderCallback, proofSubmitCallback);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class Dapp {\n");
    
    sb.append("    dappKey: ").append(toIndentedString(dappKey)).append("\n");
    sb.append("    protocol: ").append(toIndentedString(protocol)).append("\n");
    sb.append("    version: ").append(toIndentedString(version)).append("\n");
    sb.append("    ts: ").append(toIndentedString(ts)).append("\n");
    sb.append("    nonce: ").append(toIndentedString(nonce)).append("\n");
    sb.append("    os: ").append(toIndentedString(os)).append("\n");
    sb.append("    language: ").append(toIndentedString(language)).append("\n");
    sb.append("    md5: ").append(toIndentedString(md5)).append("\n");
    sb.append("    dappId: ").append(toIndentedString(dappId)).append("\n");
    sb.append("    dappName: ").append(toIndentedString(dappName)).append("\n");
    sb.append("    icon: ").append(toIndentedString(icon)).append("\n");
    sb.append("    publicKey: ").append(toIndentedString(publicKey)).append("\n");
    sb.append("    packageName: ").append(toIndentedString(packageName)).append("\n");
    sb.append("    bundleId: ").append(toIndentedString(bundleId)).append("\n");
    sb.append("    schema: ").append(toIndentedString(schema)).append("\n");
    sb.append("    website: ").append(toIndentedString(website)).append("\n");
    sb.append("    downloadUrl: ").append(toIndentedString(downloadUrl)).append("\n");
    sb.append("    depositContractAddress: ").append(toIndentedString(depositContractAddress)).append("\n");
    sb.append("    dappType: ").append(toIndentedString(dappType)).append("\n");
    sb.append("    dappCategory: ").append(toIndentedString(dappCategory)).append("\n");
    sb.append("    authLoginCallback: ").append(toIndentedString(authLoginCallback)).append("\n");
    sb.append("    payOrderCallback: ").append(toIndentedString(payOrderCallback)).append("\n");
    sb.append("    proofSubmitCallback: ").append(toIndentedString(proofSubmitCallback)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
