# Data 360 Documentation — Acme Data Cloud (Developer Edition)

_Generated 2026-10-22 14:06:38 UTC · https://example.my.salesforce.com_

## Data Model Objects (DMOs)

### Account (`ssot__Account__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_BillContactAddressId__c | Text (via DLO) |  |
| KQ_FaxPhoneId__c | Text (via DLO) |  |
| KQ_Id__c | Text (via DLO) |  |
| KQ_ParentAccountId__c | Text (via DLO) |  |
| KQ_SalesPhoneId__c | Text (via DLO) |  |
| KQ_ShippingPhoneid__c | Text (via DLO) |  |
| ssot__AccountBusinessType__c | Text (via DLO) |  |
| ssot__AccountOwnershipType__c | Text (via DLO) |  |
| ssot__AccountRatingType__c | Text (via DLO) |  |
| ssot__AccountSource__c | Text (via DLO) |  |
| ssot__AccountType__c | Text (via DLO) |  |
| ssot__AccountTypeId__c | Text (via DLO) |  |
| ssot__AccountWebsiteURL__c | Url (via DLO) |  |
| ssot__AnnualRevenueAmount__c | Number (via DLO) |  |
| ssot__BillContactAddressId__c | Text (via DLO) |  |
| ssot__CreatedDate__c | DateTime (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Description__c | Text (via DLO) |  |
| ssot__EmployeeCount__c | Number (via DLO) |  |
| ssot__FaxPhoneId__c | Phone (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__LastActivityDate__c | DateTime (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |
| ssot__Number__c | Text (via DLO) |  |
| ssot__OwnerId__c | Text (via DLO) |  |
| ssot__ParentAccountId__c | Text (via DLO) |  |
| ssot__PrimaryIndustry__c | Text (via DLO) |  |
| ssot__ProfileImageUrl__c | Url (via DLO) |  |
| ssot__SalesPhoneId__c | Text (via DLO) |  |
| ssot__ShippingPhoneid__c | Phone (via DLO) |  |
| ssot__WebsiteAddr__c | Url (via DLO) |  |

### Account Contact (`ssot__AccountContact__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_AccountId__c | Text (via DLO) |  |
| KQ_BusinessPhoneId__c | Text (via DLO) |  |
| KQ_ContactEmailId__c | Text (via DLO) |  |
| KQ_FaxPhoneId__c | Text (via DLO) |  |
| KQ_HomePhoneId__c | Text (via DLO) |  |
| KQ_Id__c | Text (via DLO) |  |
| KQ_IndividualId__c | Text (via DLO) |  |
| KQ_MailingAddressId__c | Text (via DLO) |  |
| KQ_MobilePhoneId__c | Text (via DLO) |  |
| KQ_ReportsToAccountContactId__c | Text (via DLO) |  |
| ssot__AccountId__c | Text (via DLO) |  |
| ssot__AssistantName__c | Text (via DLO) |  |
| ssot__AssistantPhone__c | Phone (via DLO) |  |
| ssot__BusinessPhoneId__c | Text (via DLO) |  |
| ssot__ContactEmailId__c | Text (via DLO) |  |
| ssot__CreatedDate__c | DateTime (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__DepartmentName__c | Text (via DLO) |  |
| ssot__FaxPhoneId__c | Phone (via DLO) |  |
| ssot__FirstName__c | Text (via DLO) |  |
| ssot__Gender__c | Text (via DLO) |  |
| ssot__HomePhoneId__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__IndividualId__c | Text (via DLO) |  |
| ssot__LastActivityDate__c | DateTime (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__LastName__c | Text (via DLO) |  |
| ssot__MailingAddressId__c | Text (via DLO) |  |
| ssot__MobilePhoneId__c | Text (via DLO) |  |
| ssot__OwnerId__c | Text (via DLO) |  |
| ssot__PersonName__c | Text (via DLO) |  |
| ssot__ReportsToAccountContactId__c | Text (via DLO) |  |
| ssot__Title__c | Text (via DLO) |  |

### Bulk Email Message (`ssot__BulkEmailMessage__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| CcAddress__c | Text (via DLO) |  |
| KQ_CampaignId__c | Text (via DLO) |  |
| KQ_Id__c | Text (via DLO) |  |
| OwnerId__c | Text (via DLO) |  |
| ReplyToName__c | Text (via DLO) |  |
| ssot__CampaignId__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__FromAddress__c | Text (via DLO) |  |
| ssot__FromName__c | Text (via DLO) |  |
| ssot__HasAttachment__c | Text (via DLO) |  |
| ssot__HTMLBodyText__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |
| ssot__ReplyToAddress__c | Text (via DLO) |  |
| ssot__ScheduledDate__c | DateTime (via DLO) |  |
| ssot__SendMechanismName__c | Text (via DLO) |  |
| ssot__Subject__c | Text (via DLO) |  |

### Business Period (`ssot__BusinessPeriod__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| ssot__BusinessPeriodType__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__FullyQualifiedLabel__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__PeriodLabel__c | Text (via DLO) |  |
| ssot__PeriodNumber__c | Number (via DLO) |  |
| ssot__QuarterLabel__c | Text (via DLO) |  |

### Campaign (`ssot__Campaign__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| KQ_ParentCampaignId__c | Text (via DLO) |  |
| ssot__ActualCostAmount__c | Number (via DLO) |  |
| ssot__BudgetedCostAmount__c | Number (via DLO) |  |
| ssot__CampaignEndDate__c | DateTime (via DLO) |  |
| ssot__CampaignStartDate__c | DateTime (via DLO) |  |
| ssot__CampaignStatus__c | Text (via DLO) |  |
| ssot__CampaignType__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Description__c | Text (via DLO) |  |
| ssot__ExpectedResponsePercent__c | Percent (via DLO) |  |
| ssot__ExpectedRevenueAmount__c | Number (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |
| ssot__ParentCampaignId__c | Text (via DLO) |  |

### Category (`ssot__Category__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| ssot__CategoryStatus__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__LabelName__c | Text (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |
| ssot__SortOrderNumber__c | Number (via DLO) |  |

### Contact Point Address (`ssot__ContactPointAddress__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| KQ_PartyId__c | Text (via DLO) |  |
| ssot__AddressLine1__c | Text (via DLO) |  |
| ssot__CityId__c | Text (via DLO) |  |
| ssot__CityName__c | Text (via DLO) |  |
| ssot__CountryId__c | Text (via DLO) |  |
| ssot__CountryName__c | Text (via DLO) |  |
| ssot__CreatedDate__c | DateTime (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__GeoLatitude__c | Number (via DLO) |  |
| ssot__GeoLongitude__c | Number (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__PartyId__c | Text (via DLO) |  |
| ssot__PostalCodeId__c | Text (via DLO) |  |
| ssot__PostalCodeText__c | Text (via DLO) |  |
| ssot__StateProvinceId__c | Text (via DLO) |  |
| ssot__StateProvinceName__c | Text (via DLO) |  |

### Contact Point Email (`ssot__ContactPointEmail__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| KQ_PartyId__c | Text (via DLO) |  |
| ssot__CreatedDate__c | DateTime (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__EmailAddress__c | Email (via DLO) |  |
| ssot__EmailLatestBounceDateTime__c | DateTime (via DLO) |  |
| ssot__EmailLatestBounceReasonText__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__PartyId__c | Text (via DLO) |  |

### Contact Point Phone (`ssot__ContactPointPhone__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| KQ_PartyId__c | Text (via DLO) |  |
| ssot__CreatedDate__c | DateTime (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__ForBusinessUse__c | Phone (via DLO) |  |
| ssot__FormattedE164PhoneNumber__c | Phone (via DLO) |  |
| ssot__ForPersonalUse__c | Phone (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__PartyId__c | Text (via DLO) |  |
| ssot__TelephoneNumber__c | Phone (via DLO) |  |

### Digital Content (`ssot__DigitalContent__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__DigitalContentType__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |

### Engagement Channel Type (`ssot__EngagementChannelType__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| ssot__ContactPointType__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |
| UsageType__c | Text (via DLO) |  |

### Financial Customer (`ssot__FinancialCustomer__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_AccountId__c | Text (via DLO) |  |
| KQ_Id__c | Text (via DLO) |  |
| ssot__AccountId__c | Text (via DLO) |  |
| ssot__CustomerRating__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |

### Individual (`ssot__Individual__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| KQ_PartyId__c | Text (via DLO) |  |
| KQ_PrimaryAccountId__c | Text (via DLO) |  |
| ssot__BirthDate__c | DateTime (via DLO) |  |
| ssot__CreatedDate__c | DateTime (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__ExternalRecordId__c | Text (via DLO) |  |
| ssot__ExternalSourceId__c | Text (via DLO) |  |
| ssot__FirstName__c | Text (via DLO) |  |
| ssot__GenderIdentity__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__LastName__c | Text (via DLO) |  |
| ssot__PartyId__c | Text (via DLO) |  |
| ssot__PersonName__c | Text (via DLO) |  |
| ssot__PhotoURL__c | Url (via DLO) |  |
| ssot__PrimaryAccountId__c | Text (via DLO) |  |
| ssot__Pronoun__c | Text (via DLO) |  |
| ssot__Salutation__c | Text (via DLO) |  |
| ssot__TitleName__c | Text (via DLO) |  |

### Market Segment (`ssot__MarketSegment__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| ssot__CreatedDate__c | DateTime (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Description__c | Text (via DLO) |  |
| ssot__ExcludeCriteriaText__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__IncludeCriteriaText__c | Text (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__LastStatusDate__c | DateTime (via DLO) |  |
| ssot__LastStatusErrorMessageText__c | Text (via DLO) |  |
| ssot__MktSegPubStatus__c | Text (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |

### Operating Hours (`ssot__OperatingHours__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Friday_EndTime__c | Text (via DLO) |  |
| ssot__Friday_StartTime__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__isActive__c | Text (via DLO) |  |
| ssot__isDefault__c | Text (via DLO) |  |
| ssot__Monday_EndTime__c | Text (via DLO) |  |
| ssot__Monday_StartTime__c | Text (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |
| ssot__Saturday_EndTime__c | Text (via DLO) |  |
| ssot__Saturday_StartTime__c | Text (via DLO) |  |
| ssot__Sunday_EndTime__c | Text (via DLO) |  |
| ssot__Sunday_StartTime__c | Text (via DLO) |  |
| ssot__Thursday_EndTime__c | Text (via DLO) |  |
| ssot__Thursday_StartTime__c | Text (via DLO) |  |
| ssot__TimeZone__c | Text (via DLO) |  |
| ssot__Tuesday_EndTime__c | Text (via DLO) |  |
| ssot__Tuesday_StartTime__c | Text (via DLO) |  |
| ssot__Wednesday_EndTime__c | Text (via DLO) |  |
| ssot__Wednesday_StartTime__c | Text (via DLO) |  |

### Opportunity Contact (`ssot__OpportunityContact__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_AccountContactId__c | Text (via DLO) |  |
| KQ_Id__c | Text (via DLO) |  |
| ssot__AccountContactId__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__IsPrimary__c | Text (via DLO) |  |
| ssot__OpportunityId__c | Text (via DLO) |  |
| ssot__OpportunitytContactRole__c | Text (via DLO) |  |

### Party (`ssot__Party__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| KQ_IndividualId__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__IndividualId__c | Text (via DLO) |  |
| ssot__PartyType__c | Text (via DLO) |  |

### Price Book (`ssot__PriceBook__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Description__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__IsActive__c | Text (via DLO) |  |
| ssot__IsArchived__c | Text (via DLO) |  |
| ssot__IsDeleted__c | Text (via DLO) |  |
| ssot__IsStandardPriceBook__c | Text (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |

### Price Book Entry (`ssot__PriceBookEntry__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| KQ_PricebookId__c | Text (via DLO) |  |
| ssot__CreatedById__c | Text (via DLO) |  |
| ssot__CreatedDate__c | DateTime (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__IsActive__c | Text (via DLO) |  |
| ssot__IsArchived__c | Text (via DLO) |  |
| ssot__IsDeleted__c | Text (via DLO) |  |
| ssot__LastModifiedById__c | Text (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |
| ssot__PricebookId__c | Text (via DLO) |  |
| ssot__ProductId__c | Text (via DLO) |  |
| ssot__SystemModstamp__c | DateTime (via DLO) |  |
| ssot__UnitListPriceAmount__c | Number (via DLO) |  |
| ssot__UseStandardPrice__c | Text (via DLO) |  |

### Product Category (`ssot__ProductCategory__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| KQ_Id__c | Text (via DLO) |  |
| KQ_ParentCategoryId__c | Text (via DLO) |  |
| ssot__CreatedDate__c | DateTime (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Description__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__IsNavigational__c | Text (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |
| ssot__ParentCategory__c | Text (via DLO) |  |
| ssot__ParentCategoryId__c | Text (via DLO) |  |
| ssot__ProductCatalogId__c | Text (via DLO) |  |

### Promotion (`ssot__Promotion__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| CreatedById__c | Text (via DLO) |  |
| KQ_Id__c | Text (via DLO) |  |
| KQ_PrimaryCampaignId__c | Text (via DLO) |  |
| ssot__CreatedDate__c | DateTime (via DLO) |  |
| ssot__DataSourceId__c | Text (via DLO) |  |
| ssot__DataSourceObjectId__c | Text (via DLO) |  |
| ssot__Description__c | Text (via DLO) |  |
| ssot__DiscountExclusivityTypeId__c | Text (via DLO) |  |
| ssot__DisplayName__c | Text (via DLO) |  |
| ssot__Id__c | Text (via DLO) |  |
| ssot__IsActive__c | Text (via DLO) |  |
| ssot__IsAutomatic__c | Text (via DLO) |  |
| ssot__IsCommercePromotion__c | Text (via DLO) |  |
| ssot__LastModifiedDate__c | DateTime (via DLO) |  |
| ssot__Name__c | Text (via DLO) |  |
| ssot__ObjectiveText__c | Text (via DLO) |  |
| ssot__PrimaryCampaignId__c | Text (via DLO) |  |

### Static Currency Rates Home (`StaticCurrencyRates_Home__dlm`)

| Name | Type | Key |
| --- | --- | --- |
| DataSourceId__c | Unknown |  |
| DataSourceObjectId__c | Unknown |  |
| FromISOCurrencyCode__c | Unknown |  |
| Id__c | Unknown |  |
| InternalOrganizationId__c | Unknown |  |
| KQ_Id__c | Unknown |  |
| RateDenominatorNumber__c | Unknown |  |
| RateNumeratorNumber__c | Unknown |  |
| ToISOCurrencyCode__c | Unknown |  |

## Data Lake Objects (DLOs)

### Account_Home (`Account_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| AccountNumber | Text |  |
| AccountSource | Text |  |
| Active_c | Text |  |
| AnnualRevenue | Number |  |
| BillingCity | Text |  |
| BillingCountry | Text |  |
| BillingCountryCode | Text |  |
| BillingGeocodeAccuracy | Text |  |
| BillingLatitude | Number |  |
| BillingLongitude | Number |  |
| BillingPostalCode | Text |  |
| BillingState | Text |  |
| BillingStateCode | Text |  |
| BillingStreet | Text |  |
| cdp_sys_SourceVersion | Text |  |
| CleanStatus | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| CustomerPriority_c | Text |  |
| DandbCompanyId | Text |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| Description | Text |  |
| DunsNumber | Text |  |
| Fax | Phone |  |
| Id | Text | PrimaryKey |
| Industry | Text |  |
| IsDeleted | Text |  |
| Jigsaw | Text |  |
| JigsawCompanyId | Text |  |
| KQ_Fax | Text |  |
| KQ_Id | Text |  |
| KQ_ParentId | Text |  |
| KQ_Phone | Text |  |
| LastActivityDate | DateTime |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| LastReferencedDate | DateTime |  |
| LastViewedDate | DateTime |  |
| MasterRecordId | Text |  |
| NaicsCode | Text |  |
| NaicsDesc | Text |  |
| Name | Text |  |
| NumberOfEmployees | Number |  |
| NumberofLocations_c | Number |  |
| OperatingHoursId | Text |  |
| OwnerId | Text |  |
| Ownership | Text |  |
| ParentId | Text |  |
| Phone | Phone |  |
| PhotoUrl | Url |  |
| Rating | Text |  |
| SfdcOrganizationId | Text |  |
| ShippingCity | Text |  |
| ShippingCountry | Text |  |
| ShippingCountryCode | Text |  |
| ShippingGeocodeAccuracy | Text |  |
| ShippingLatitude | Number |  |
| ShippingLongitude | Number |  |
| ShippingPostalCode | Text |  |
| ShippingState | Text |  |
| ShippingStateCode | Text |  |
| ShippingStreet | Text |  |
| Sic | Text |  |
| SicDesc | Text |  |
| Site | Text |  |
| SLA_c | Text |  |
| SLAExpirationDate_c | Date |  |
| SLASerialNumber_c | Text |  |
| SystemModstamp | DateTime |  |
| TickerSymbol | Text |  |
| Tradestyle | Text |  |
| Type | Text |  |
| UpsellOpportunity_c | Text |  |
| Website | Url |  |
| YearStarted | Text |  |

### BusinessHours_Home (`BusinessHours_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| FridayEndTime | Text |  |
| FridayStartTime | Text |  |
| Id | Text | PrimaryKey |
| IsActive | Text |  |
| IsDefault | Text |  |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| LastViewedDate | DateTime |  |
| MondayEndTime | Text |  |
| MondayStartTime | Text |  |
| Name | Text |  |
| SaturdayEndTime | Text |  |
| SaturdayStartTime | Text |  |
| SfdcOrganizationId | Text |  |
| SundayEndTime | Text |  |
| SundayStartTime | Text |  |
| SystemModstamp | DateTime |  |
| ThursdayEndTime | Text |  |
| ThursdayStartTime | Text |  |
| TimeZoneSidKey | Text |  |
| TuesdayEndTime | Text |  |
| TuesdayStartTime | Text |  |
| WednesdayEndTime | Text |  |
| WednesdayStartTime | Text |  |

### Campaign_Home (`Campaign_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| ActualCost | Number |  |
| AmountAllOpportunities | Number |  |
| AmountWonOpportunities | Number |  |
| BudgetedCost | Number |  |
| CampaignMemberRecordTypeId | Text |  |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| Description | Text |  |
| EndDate | DateTime |  |
| ExpectedResponse | Percent |  |
| ExpectedRevenue | Number |  |
| HierarchyActualCost | Number |  |
| HierarchyAmountAllOpportunities | Number |  |
| HierarchyAmountWonOpportunities | Number |  |
| HierarchyBudgetedCost | Number |  |
| HierarchyExpectedRevenue | Number |  |
| HierarchyNumberOfContacts | Number |  |
| HierarchyNumberOfConvertedLeads | Number |  |
| HierarchyNumberOfLeads | Number |  |
| HierarchyNumberOfOpportunities | Number |  |
| HierarchyNumberOfResponses | Number |  |
| HierarchyNumberOfWonOpportunities | Number |  |
| HierarchyNumberSent | Number |  |
| Id | Text | PrimaryKey |
| IsActive | Text |  |
| IsDeleted | Text |  |
| KQ_Id | Text |  |
| LastActivityDate | DateTime |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| LastReferencedDate | DateTime |  |
| LastViewedDate | DateTime |  |
| Name | Text |  |
| NumberOfContacts | Number |  |
| NumberOfConvertedLeads | Number |  |
| NumberOfLeads | Number |  |
| NumberOfOpportunities | Number |  |
| NumberOfResponses | Number |  |
| NumberOfWonOpportunities | Number |  |
| NumberSent | Number |  |
| OwnerId | Text |  |
| ParentId | Text |  |
| SfdcOrganizationId | Text |  |
| StartDate | DateTime |  |
| Status | Text |  |
| SystemModstamp | DateTime |  |
| Type | Text |  |

### Contact_Home (`Contact_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| AccountId | Text |  |
| AssistantName | Text |  |
| AssistantPhone | Phone |  |
| Birthdate | DateTime |  |
| BuyerAttributes | Text |  |
| cdp_sys_SourceVersion | Text |  |
| CleanStatus | Text |  |
| ContactSource | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| Department | Text |  |
| Description | Text |  |
| DoNotCall | Text |  |
| Email | Email |  |
| EmailBouncedDate | DateTime |  |
| EmailBouncedReason | Text |  |
| Fax | Phone |  |
| FirstName | Text |  |
| GenderIdentity | Text |  |
| HasOptedOutOfEmail | Text |  |
| HasOptedOutOfFax | Text |  |
| HomePhone | Phone |  |
| Id | Text | PrimaryKey |
| IndividualId | Text |  |
| IsDeleted | Text |  |
| IsEmailBounced | Text |  |
| IsPriorityRecord | Text |  |
| Jigsaw | Text |  |
| JigsawContactId | Text |  |
| KQ_AccountId | Text |  |
| KQ_Fax | Text |  |
| KQ_Id | Text |  |
| KQ_ReportsToId | Text |  |
| Languages_c | Text |  |
| LastActivityDate | DateTime |  |
| LastCURequestDate | DateTime |  |
| LastCUUpdateDate | DateTime |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| LastName | Text |  |
| LastReferencedDate | DateTime |  |
| LastViewedDate | DateTime |  |
| LeadSource | Text |  |
| Level_c | Text |  |
| MailingCity | Text |  |
| MailingCountry | Text |  |
| MailingCountryCode | Text |  |
| MailingGeocodeAccuracy | Text |  |
| MailingLatitude | Number |  |
| MailingLongitude | Number |  |
| MailingPostalCode | Text |  |
| MailingState | Text |  |
| MailingStateCode | Text |  |
| MailingStreet | Text |  |
| MasterRecordId | Text |  |
| MobilePhone | Phone |  |
| Name | Text |  |
| OtherCity | Text |  |
| OtherCountry | Text |  |
| OtherCountryCode | Text |  |
| OtherGeocodeAccuracy | Text |  |
| OtherLatitude | Number |  |
| OtherLongitude | Number |  |
| OtherPhone | Phone |  |
| OtherPostalCode | Text |  |
| OtherState | Text |  |
| OtherStateCode | Text |  |
| OtherStreet | Text |  |
| OwnerId | Text |  |
| Phone | Phone |  |
| PhotoUrl | Url |  |
| Pronouns | Text |  |
| ReportsToId | Text |  |
| Salutation | Text |  |
| SfdcOrganizationId | Text |  |
| SystemModstamp | DateTime |  |
| Title | Text |  |

### DataCategory_Home (`DataCategory_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataCategoryGroupId | Text |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| DeveloperName | Text |  |
| Id | Text | PrimaryKey |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| MasterLabel | Text |  |
| ParentId | Text |  |
| SfdcOrganizationId | Text |  |
| SortOrder | Number |  |
| SortStyle | Text |  |
| SystemModstamp | DateTime |  |

### DataCategoryGroup_Home (`DataCategoryGroup_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| Description | Text |  |
| DeveloperName | Text |  |
| Id | Text | PrimaryKey |
| IsDeleted | Text |  |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| MasterLabel | Text |  |
| OptionsFlagRecordsRecategorizationInProg | Text |  |
| SfdcOrganizationId | Text |  |
| Status | Text |  |
| SystemModstamp | DateTime |  |

### EngagementChannelType_Home (`EngagementChannelType_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| cdp_sys_SourceVersion | Text |  |
| ChannelTypeCode | Text |  |
| ContactPointType | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| Id | Text | PrimaryKey |
| IsActive | Text |  |
| IsDeleted | Text |  |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| LastReferencedDate | DateTime |  |
| LastViewedDate | DateTime |  |
| Name | Text |  |
| OwnerId | Text |  |
| SfdcOrganizationId | Text |  |
| SystemModstamp | DateTime |  |
| UsageType | Text |  |

### EventRelation_Home (`EventRelation_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| EventId | Text |  |
| Id | Text | PrimaryKey |
| IsDeleted | Text |  |
| IsOrganizer | Text |  |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| RelationId | Text |  |
| RespondedDate | DateTime |  |
| Response | Text |  |
| SfdcOrganizationId | Text |  |
| Status | Text |  |
| SystemModstamp | DateTime |  |

### ListEmail_Home (`ListEmail_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| CampaignId | Text |  |
| CcAddress | Text |  |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| DataSpaceId | Text |  |
| FromAddress | Text |  |
| FromName | Text |  |
| HasAttachment | Text |  |
| HtmlBody | Text |  |
| Id | Text | PrimaryKey |
| IsDeleted | Text |  |
| IsEmailArchiveRequired | Text |  |
| IsSyntheticCcEnabled | Text |  |
| IsTracked | Text |  |
| KQ_CampaignId | Text |  |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| LastReferencedDate | DateTime |  |
| LastViewedDate | DateTime |  |
| Name | Text |  |
| OwnerId | Text |  |
| RelatedToId | Text |  |
| ReplyToAddress | Text |  |
| ReplyToName | Text |  |
| ScheduledDate | DateTime |  |
| SentVia | Text |  |
| SfdcOrganizationId | Text |  |
| Status | Text |  |
| Subject | Text |  |
| SystemModstamp | DateTime |  |
| TextBody | Text |  |
| TotalSent | Number |  |

### ManagedContent_Home (`ManagedContent_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| ApiName | Text |  |
| AuthoredManagedContentSpaceId | Text |  |
| cdp_sys_SourceVersion | Text |  |
| ContentKey | Text |  |
| ContentTypeFullyQualifiedName | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| DataSpaceId | Text |  |
| ExternalId | Text |  |
| Id | Text | PrimaryKey |
| IsDeleted | Text |  |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| Name | Text |  |
| PrimaryLanguage | Text |  |
| SfdcOrganizationId | Text |  |
| SystemModstamp | DateTime |  |

### MarketSegment_Home (`MarketSegment_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| AdditionalMetadataInfo | Text |  |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataGraphId | Text |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| DataSpaceId | Text |  |
| Description | Text |  |
| ExcludeCriteria | Text |  |
| GroupSortLimitFilterCriteria | Text |  |
| Id | Text | PrimaryKey |
| IncludeCriteria | Text |  |
| IsCurrentSaveApproxCount | Text |  |
| IsDeleted | Text |  |
| IsPrevSaveApproxCount | Text |  |
| IsRemote | Text |  |
| IsSeedSegment | Text |  |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| LastPublishedEndDateTime | DateTime |  |
| LastPublishStatusDateTime | DateTime |  |
| LastPublishStatusErrorCode | Text |  |
| LastReferencedDate | DateTime |  |
| LastSeedModelRunDateTime | DateTime |  |
| LastSeedModelStatusDateTime | DateTime |  |
| LastSeedModelStatusErrorCode | Text |  |
| LastSegmentCountEndDateTime | DateTime |  |
| LastSegmentExcludedCount | Number |  |
| LastSegmentExcludedCountError | Number |  |
| LastSegmentIncludedCount | Number |  |
| LastSegmentMemberCount | Number |  |
| LastSegmentMemberCountError | Number |  |
| LastSegmentRemainderCount | Number |  |
| LastSegmentStatusDateTime | DateTime |  |
| LastSegmentStatusErrorCode | Text |  |
| LastSegmentStatusErrorDetails | Text |  |
| LastSegmentTotalCount | Number |  |
| LastViewedDate | DateTime |  |
| LookbackPeriod | Text |  |
| MarketSegmentDefinitionId | Text |  |
| MarketSegmentType | Text |  |
| Name | Text |  |
| NextPublishDateTime | DateTime |  |
| OwnedBy | Text |  |
| PublishScheduleEndDate | DateTime |  |
| PublishScheduleEndDateTime | DateTime |  |
| PublishScheduleInfo | Text |  |
| PublishScheduleInterval | Text |  |
| PublishScheduleStartDateTime | DateTime |  |
| PublishStatus | Text |  |
| PublishType | Text |  |
| SeedModelStatus | Text |  |
| SeedSimilarity | Text |  |
| SeedSimilarityHighToMedium | Number |  |
| SeedSimilarityMediumToLow | Number |  |
| SegmentMembershipDataModelList | Text |  |
| SegmentMembershipTable | Text |  |
| SegmentOnId | Text |  |
| SegmentStatus | Text |  |
| SfdcOrganizationId | Text |  |
| SourceMarketSegment | Text |  |
| SystemModstamp | DateTime |  |

### OpportunityContactRole_Home (`OpportunityContactRole_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| cdp_sys_SourceVersion | Text |  |
| ContactId | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| Id | Text | PrimaryKey |
| IsDeleted | Text |  |
| IsPrimary | Text |  |
| KQ_ContactId | Text |  |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| OpportunityId | Text |  |
| Role | Text |  |
| SfdcOrganizationId | Text |  |
| SystemModstamp | DateTime |  |

### Period_Home (`Period_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| cdp_sys_SourceVersion | Text |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| EndDate | DateTime |  |
| FiscalYearSettingsId | Text |  |
| FullyQualifiedLabel | Text |  |
| Id | Text | PrimaryKey |
| IsForecastPeriod | Text |  |
| KQ_Id | Text |  |
| Number | Number |  |
| PeriodLabel | Text |  |
| QuarterLabel | Text |  |
| SfdcOrganizationId | Text |  |
| StartDate | DateTime |  |
| SystemModstamp | DateTime |  |
| Type | Text |  |

### Pricebook2_Home (`Pricebook2_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| Description | Text |  |
| Id | Text | PrimaryKey |
| IsActive | Text |  |
| IsArchived | Text |  |
| IsDeleted | Text |  |
| IsStandard | Text |  |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| LastReferencedDate | DateTime |  |
| LastViewedDate | DateTime |  |
| Name | Text |  |
| SfdcOrganizationId | Text |  |
| SystemModstamp | DateTime |  |

### PricebookEntry_Home (`PricebookEntry_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| Id | Text | PrimaryKey |
| IsActive | Text |  |
| IsArchived | Text |  |
| IsDeleted | Text |  |
| KQ_Id | Text |  |
| KQ_Pricebook2Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| Name | Text |  |
| Pricebook2Id | Text |  |
| Product2Id | Text |  |
| ProductCode | Text |  |
| SfdcOrganizationId | Text |  |
| SystemModstamp | DateTime |  |
| UnitPrice | Number |  |
| UseStandardPrice | Text |  |

### ProductCategory_Home (`ProductCategory_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| CatalogId | Text |  |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| Description | Text |  |
| Id | Text | PrimaryKey |
| IsDeleted | Text |  |
| IsNavigational | Text |  |
| KQ_Id | Text |  |
| KQ_ParentCategoryId | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| LastReferencedDate | DateTime |  |
| LastViewedDate | DateTime |  |
| Name | Text |  |
| NumberOfProducts | Number |  |
| ParentCategoryId | Text |  |
| SfdcOrganizationId | Text |  |
| SortOrder | Number |  |
| SystemModstamp | DateTime |  |

### Promotion_Home (`Promotion_Home__dll`)

| Name | Type | Key |
| --- | --- | --- |
| AreQualItemsExclFromDiscounts | Text |  |
| CampaignId | Text |  |
| cdp_sys_SourceVersion | Text |  |
| CreatedById | Text |  |
| CreatedDate | DateTime |  |
| DataSource | Text |  |
| DataSourceObject | Text |  |
| Description | Text |  |
| DiscountOrder | Text |  |
| DiscountRestriction | Text |  |
| DisplayName | Text |  |
| EndDateTime | DateTime |  |
| ExclusivityType | Text |  |
| Id | Text | PrimaryKey |
| IsActive | Text |  |
| IsApproachingDiscountApplicable | Text |  |
| IsAutomatic | Text |  |
| IsCommercePromotion | Text |  |
| IsDeleted | Text |  |
| IsQualCriteriaNotRequiredPerApplication | Text |  |
| IsTiered | Text |  |
| KQ_CampaignId | Text |  |
| KQ_Id | Text |  |
| LastModifiedById | Text |  |
| LastModifiedDate | DateTime |  |
| LastReferencedDate | DateTime |  |
| LastViewedDate | DateTime |  |
| MaximumUsageCount | Number |  |
| Name | Text |  |
| Objective | Text |  |
| OwnerId | Text |  |
| PriorityNumber | Number |  |
| QualifierCriteria | Text |  |
| SfdcOrganizationId | Text |  |
| StartDateTime | DateTime |  |
| SystemModstamp | DateTime |  |
| TargetCriteria | Text |  |
| TermsAndConditions | Text |  |

## Data Streams

Source and refresh metadata per stream. **ApiName** is the DLO it populates (see the Data Lake Objects section above).

| DataSource | ObjectLabel | ApiName | Category | EventTimeField | PrimaryKey | FormulaField | FormulaCalculation | OrgUnitIdentifier | ScheduleFrequency | RefreshMode | DEExtractionMode | StreamName |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SalesforceDotCom | Account_Home | Account_Home__dll | Profile |  | Id |  |  |  | BATCH | UPSERT |  | Account_Home |
| SalesforceDotCom | BusinessHours_Home | BusinessHours_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | BusinessHours_Home |
| SalesforceDotCom | Campaign_Home | Campaign_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | Campaign_Home |
| SalesforceDotCom | Contact_Home | Contact_Home__dll | Profile |  | Id |  |  |  | BATCH | UPSERT |  | Contact_Home |
| SalesforceDotCom | DataCategory_Home | DataCategory_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | DataCategory_Home |
| SalesforceDotCom | DataCategoryGroup_Home | DataCategoryGroup_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | DataCategoryGroup_Home |
| SalesforceDotCom | EngagementChannelType_Home | EngagementChannelType_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | EngagementChannelType_Home |
| SalesforceDotCom | EventRelation_Home | EventRelation_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | EventRelation_Home |
| SalesforceDotCom | ListEmail_Home | ListEmail_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | ListEmail_Home |
| SalesforceDotCom | ManagedContent_Home | ManagedContent_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | ManagedContent_Home |
| SalesforceDotCom | MarketSegment_Home | MarketSegment_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | MarketSegment_Home |
| SalesforceDotCom | OpportunityContactRole_Home | OpportunityContactRole_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | OpportunityContactRole_Home |
| SalesforceDotCom | Period_Home | Period_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | Period_Home |
| SalesforceDotCom | Pricebook2_Home | Pricebook2_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | Pricebook2_Home |
| SalesforceDotCom | PricebookEntry_Home | PricebookEntry_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | PricebookEntry_Home |
| SalesforceDotCom | ProductCategory_Home | ProductCategory_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | ProductCategory_Home |
| SalesforceDotCom | Promotion_Home | Promotion_Home__dll | Other |  | Id |  |  |  | BATCH | UPSERT |  | Promotion_Home |

## Field Mapping (Streams → DLO)

One row per Data Lake field. **DLO API Name** is the Data Lake Object the stream populates. **Foreign Key** is heuristic — flagged for fields whose API name starts with `KQ_` (Data Cloud Key Qualifier pattern). **Nullable** is shown only where the source exposes it; `/ssot/data-streams` does not, so it stays blank for these streams (it is never guessed).

| Mapped Data Stream | DLO API Name | Field Label Source | Field Label DLO | Data Type | Primary Key | Data Source | Foreign Key | Nullable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Account_Home | Account_Home__dll | AccountNumber | Account Number | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | AccountSource | Account Source | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Active__c | Active | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | AnnualRevenue | Annual Revenue | Number | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | BillingCity | Billing City | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | BillingCountry | Billing Country | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | BillingCountryCode | Billing Country Code | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | BillingGeocodeAccuracy | Billing Geocode Accuracy | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | BillingLatitude | Billing Latitude | Number | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | BillingLongitude | Billing Longitude | Number | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | BillingPostalCode | Billing Zip/Postal Code | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | BillingState | Billing State/Province | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | BillingStateCode | Billing State/Province Code | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | BillingStreet | Billing Street | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | CleanStatus | Clean Status | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | CustomerPriority__c | Customer Priority | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | DandbCompanyId | D&amp;B Company ID | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Description | Account Description | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | DunsNumber | D-U-N-S Number | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Fax | Account Fax | Phone | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Id | Account ID | Text | Yes | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Industry | Industry | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Jigsaw | Data.com Key | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | JigsawCompanyId | Jigsaw Company ID | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll |  | KQ_Fax | Text | No | SalesforceDotCom | Yes |  |
| Account_Home | Account_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| Account_Home | Account_Home__dll |  | KQ_ParentId | Text | No | SalesforceDotCom | Yes |  |
| Account_Home | Account_Home__dll |  | KQ_Phone | Text | No | SalesforceDotCom | Yes |  |
| Account_Home | Account_Home__dll | LastActivityDate | Last Activity | DateTime | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | LastReferencedDate | Last Referenced Date | DateTime | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | LastViewedDate | Last Viewed Date | DateTime | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | MasterRecordId | Master Record ID | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | NaicsCode | NAICS Code | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | NaicsDesc | NAICS Description | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Name | Account Name | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | NumberOfEmployees | Employees | Number | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | NumberofLocations__c | Number of Locations | Number | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | OperatingHoursId | Operating Hour ID | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | OwnerId | Owner ID | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Ownership | Ownership | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ParentId | Parent Account ID | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Phone | Account Phone | Phone | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | PhotoUrl | Photo URL | Url | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Rating | Account Rating | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ShippingCity | Shipping City | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ShippingCountry | Shipping Country | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ShippingCountryCode | Shipping Country Code | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ShippingGeocodeAccuracy | Shipping Geocode Accuracy | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ShippingLatitude | Shipping Latitude | Number | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ShippingLongitude | Shipping Longitude | Number | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ShippingPostalCode | Shipping Zip/Postal Code | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ShippingState | Shipping State/Province | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ShippingStateCode | Shipping State/Province Code | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | ShippingStreet | Shipping Street | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Sic | SIC Code | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | SicDesc | SIC Description | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Site | Account Site | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | SLA__c | SLA | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | SLAExpirationDate__c | SLA Expiration Date | Date | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | SLASerialNumber__c | SLA Serial Number | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | TickerSymbol | Ticker Symbol | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Tradestyle | Tradestyle | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Type | Account Type | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | UpsellOpportunity__c | Upsell Opportunity | Text | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | Website | Website | Url | No | SalesforceDotCom |  |  |
| Account_Home | Account_Home__dll | YearStarted | Year Started | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | FridayEndTime | Friday End | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | FridayStartTime | Friday Start | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | Id | Business Hours ID | Text | Yes | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | IsActive | Active | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | IsDefault | Default Business Hours | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| BusinessHours_Home | BusinessHours_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | LastViewedDate | Last Viewed Date | DateTime | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | MondayEndTime | Monday End | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | MondayStartTime | Monday Start | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | Name | Business Hours Name | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | SaturdayEndTime | Saturday End | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | SaturdayStartTime | Saturday Start | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | SundayEndTime | Sunday End | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | SundayStartTime | Sunday Start | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | ThursdayEndTime | Thursday End | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | ThursdayStartTime | Thursday Start | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | TimeZoneSidKey | Time Zone | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | TuesdayEndTime | Tuesday End | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | TuesdayStartTime | Tuesday Start | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | WednesdayEndTime | Wednesday End | Text | No | SalesforceDotCom |  |  |
| BusinessHours_Home | BusinessHours_Home__dll | WednesdayStartTime | Wednesday Start | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | ActualCost | Actual Cost in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | AmountAllOpportunities | Value Opportunities in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | AmountWonOpportunities | Value Won Opportunities in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | BudgetedCost | Budgeted Cost in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | CampaignMemberRecordTypeId | Record Type ID | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | Description | Description | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | EndDate | End Date | DateTime | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | ExpectedResponse | Expected Response (%) | Percent | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | ExpectedRevenue | Expected Revenue in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyActualCost | Actual Cost in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyAmountAllOpportunities | Value Opportunities in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyAmountWonOpportunities | Value Won Opportunities in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyBudgetedCost | Budgeted Cost in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyExpectedRevenue | Expected Revenue in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyNumberOfContacts | Contacts in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyNumberOfConvertedLeads | Converted Leads in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyNumberOfLeads | Leads in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyNumberOfOpportunities | Opportunities in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyNumberOfResponses | Responses in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyNumberOfWonOpportunities | Won Opportunities in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | HierarchyNumberSent | Num Sent in Hierarchy | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | Id | Campaign ID | Text | Yes | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | IsActive | Active | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| Campaign_Home | Campaign_Home__dll | LastActivityDate | Last Activity | DateTime | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | LastReferencedDate | Last Referenced Date | DateTime | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | LastViewedDate | Last Viewed Date | DateTime | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | Name | Name | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | NumberOfContacts | Contacts in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | NumberOfConvertedLeads | Converted Leads in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | NumberOfLeads | Leads in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | NumberOfOpportunities | Opportunities in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | NumberOfResponses | Responses in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | NumberOfWonOpportunities | Won Opportunities in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | NumberSent | Num Sent in Campaign | Number | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | OwnerId | Owner ID | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | ParentId | Parent Campaign ID | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | StartDate | Start Date | DateTime | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | Status | Status | Text | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| Campaign_Home | Campaign_Home__dll | Type | Type | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | AccountId | Account ID | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | AssistantName | Assistant&#39;s Name | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | AssistantPhone | Asst. Phone | Phone | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Birthdate | Birthdate | DateTime | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | BuyerAttributes | Buyer Attributes | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | CleanStatus | Clean Status | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | ContactSource | Creation Source | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Department | Department | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Description | Contact Description | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | DoNotCall | Do Not Call | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Email | Email | Email | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | EmailBouncedDate | Email Bounced Date | DateTime | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | EmailBouncedReason | Email Bounced Reason | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Fax | Business Fax | Phone | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | FirstName | First Name | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | GenderIdentity | Gender Identity | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | HasOptedOutOfEmail | Email Opt Out | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | HasOptedOutOfFax | Fax Opt Out | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | HomePhone | Home Phone | Phone | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Id | Contact ID | Text | Yes | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | IndividualId | Individual ID | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | IsEmailBounced | Is Email Bounced | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | IsPriorityRecord | Important | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Jigsaw | Data.com Key | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | JigsawContactId | Jigsaw Contact ID | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll |  | KQ_AccountId | Text | No | SalesforceDotCom | Yes |  |
| Contact_Home | Contact_Home__dll |  | KQ_Fax | Text | No | SalesforceDotCom | Yes |  |
| Contact_Home | Contact_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| Contact_Home | Contact_Home__dll |  | KQ_ReportsToId | Text | No | SalesforceDotCom | Yes |  |
| Contact_Home | Contact_Home__dll | Languages__c | Languages | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | LastActivityDate | Last Activity | DateTime | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | LastCURequestDate | Last Stay-in-Touch Request Date | DateTime | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | LastCUUpdateDate | Last Stay-in-Touch Save Date | DateTime | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | LastName | Last Name | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | LastReferencedDate | Last Referenced Date | DateTime | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | LastViewedDate | Last Viewed Date | DateTime | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | LeadSource | Lead Source | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Level__c | Level | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MailingCity | Mailing City | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MailingCountry | Mailing Country | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MailingCountryCode | Mailing Country Code | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MailingGeocodeAccuracy | Mailing Geocode Accuracy | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MailingLatitude | Mailing Latitude | Number | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MailingLongitude | Mailing Longitude | Number | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MailingPostalCode | Mailing Zip/Postal Code | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MailingState | Mailing State/Province | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MailingStateCode | Mailing State/Province Code | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MailingStreet | Mailing Street | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MasterRecordId | Master Record ID | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | MobilePhone | Mobile Phone | Phone | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Name | Full Name | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherCity | Other City | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherCountry | Other Country | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherCountryCode | Other Country Code | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherGeocodeAccuracy | Other Geocode Accuracy | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherLatitude | Other Latitude | Number | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherLongitude | Other Longitude | Number | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherPhone | Other Phone | Phone | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherPostalCode | Other Zip/Postal Code | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherState | Other State/Province | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherStateCode | Other State/Province Code | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OtherStreet | Other Street | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | OwnerId | Owner ID | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Phone | Business Phone | Phone | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | PhotoUrl | Photo URL | Url | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Pronouns | Pronouns | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | ReportsToId | Reports To ID | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Salutation | Salutation | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| Contact_Home | Contact_Home__dll | Title | Title | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | DataCategoryGroupId | Data Category Type ID | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | DeveloperName | Developer Name | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | Id | Data Category ID | Text | Yes | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| DataCategory_Home | DataCategory_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | MasterLabel | Label | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | ParentId | Parent ID | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | SortOrder | Sort Order | Number | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | SortStyle | Subcategory Sort Style | Text | No | SalesforceDotCom |  |  |
| DataCategory_Home | DataCategory_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | Description | Description | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | DeveloperName | Developer Name | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | Id | Data Category Type ID | Text | Yes | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | MasterLabel | Label | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll |  | recordsRecategorizationInProgress | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | Status | Status | Text | No | SalesforceDotCom |  |  |
| DataCategoryGroup_Home | DataCategoryGroup_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | ChannelTypeCode | Channel Type Code | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | ContactPointType | Contact Point Type | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | Id | Engagement Channel Type ID | Text | Yes | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | IsActive | Active | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | LastReferencedDate | Last Referenced Date | DateTime | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | LastViewedDate | Last Viewed Date | DateTime | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | Name | Name | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | OwnerId | Owner ID | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| EngagementChannelType_Home | EngagementChannelType_Home__dll | UsageType | Usage Type | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | EventId | Event ID | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | Id | Event Relation ID | Text | Yes | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | IsOrganizer | Is Organizer | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| EventRelation_Home | EventRelation_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | RelationId | Relation ID | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | RespondedDate | Response Date | DateTime | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | Response | Response | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | Status | Status | Text | No | SalesforceDotCom |  |  |
| EventRelation_Home | EventRelation_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | CampaignId | Campaign ID | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | CcAddress | CC Address | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | DataSpaceId | Data Space ID | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | FromAddress | From Address | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | FromName | From Name | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | HasAttachment | Has Attachment | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | HtmlBody | Html Body | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | Id | List Email ID | Text | Yes | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | IsEmailArchiveRequired | Is Email Archive Required | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | IsSyntheticCcEnabled | Synthetic CC Enabled | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | IsTracked | Is Tracked | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll |  | KQ_CampaignId | Text | No | SalesforceDotCom | Yes |  |
| ListEmail_Home | ListEmail_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| ListEmail_Home | ListEmail_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | LastReferencedDate | Last Referenced Date | DateTime | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | LastViewedDate | Last Viewed Date | DateTime | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | Name | Name | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | OwnerId | Owner ID | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | RelatedToId | RelatedTo ID | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | ReplyToAddress | Reply To Address | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | ReplyToName | Reply To Name | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | ScheduledDate | Scheduled Date | DateTime | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | SentVia | Sent Via | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | Status | Status | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | Subject | Subject | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | TextBody | Text Body | Text | No | SalesforceDotCom |  |  |
| ListEmail_Home | ListEmail_Home__dll | TotalSent | Total Sent | Number | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | ApiName | API Name | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | AuthoredManagedContentSpaceId | Managed Content Space ID | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | ContentKey | Content Key | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | ContentTypeFullyQualifiedName | Content Type Fully Qualified Name | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | DataSpaceId | Data Space ID | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | ExternalId | External Id | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | Id | Managed Content ID | Text | Yes | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| ManagedContent_Home | ManagedContent_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | Name | Name | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | PrimaryLanguage | Primary Language | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| ManagedContent_Home | ManagedContent_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | AdditionalMetadataInfo | Additional Metadata Info | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | DataGraphId | Data Graph ID | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | DataSpaceId | Data Space ID | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | Description | Segment Description | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | ExcludeCriteria | Exclude Criteria | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | GroupSortLimitFilterCriteria | Advanced Criteria | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | Id | Segment ID | Text | Yes | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | IncludeCriteria | Include Criteria | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | IsCurrentSaveApproxCount | Is Current Count Approx | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | IsPrevSaveApproxCount | Is Previous Count Approx | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | IsRemote | Is Remote | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | IsSeedSegment | Is Seed Segment | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastPublishedEndDateTime | Last Publish Completed | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastPublishStatusDateTime | Last Publish Status Date Time | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastPublishStatusErrorCode | Last Publish Status Error Code | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastReferencedDate | Last Referenced Date | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSeedModelRunDateTime | Last Seed Model Run Date Time | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSeedModelStatusDateTime | Last Seed Model Status Date Time | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSeedModelStatusErrorCode | Last Seed Model Status Error Code | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentCountEndDateTime | Last Segment Count End Date Time | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentExcludedCount | Population Excluded | Number | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentExcludedCountError | Approximate Segment Population Excluded | Number | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentIncludedCount | Included Population | Number | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentMemberCount | Population | Number | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentMemberCountError | Approximate Segment Population Absolute | Number | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentRemainderCount | Population Remainder | Number | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentStatusDateTime | Segment Status Last Updated | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentStatusErrorCode | Segment Status Error Code | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentStatusErrorDetails | Segment Status Error Details | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastSegmentTotalCount | Total Population | Number | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LastViewedDate | Last Viewed Date | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | LookbackPeriod | Lookback Period | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | MarketSegmentDefinitionId | Market Segment Definition ID | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | MarketSegmentType | Segment Type | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | Name | Segment Name | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | NextPublishDateTime | Next Publish Date Time | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | OwnedBy | Owned By Connection | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | PublishScheduleEndDate | Expiration Date | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | PublishScheduleEndDateTime | Publish Schedule End Date and Time | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | PublishScheduleInfo | Publish Schedule Details | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | PublishScheduleInterval | Publish Interval | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | PublishScheduleStartDateTime | Publish Schedule Start Date and Time | DateTime | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | PublishStatus | Publish Status | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | PublishType | Publish Type | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SeedModelStatus | Seed Model Status | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SeedSimilarity | Similarity | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SeedSimilarityHighToMedium | Similarity High to Medium | Number | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SeedSimilarityMediumToLow | Similarity Medium to Low | Number | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SegmentMembershipDataModelList | Segment Membership Data Models | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SegmentMembershipTable | Segment Membership data model object nam | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SegmentOnId | Data Model Object ID | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SegmentStatus | Segment Status | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SourceMarketSegment | Source Market Segment | Text | No | SalesforceDotCom |  |  |
| MarketSegment_Home | MarketSegment_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | ContactId | Contact ID | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | Id | Contact Role ID | Text | Yes | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | IsPrimary | Primary | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll |  | KQ_ContactId | Text | No | SalesforceDotCom | Yes |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | OpportunityId | Opportunity ID | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | Role | Role | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| OpportunityContactRole_Home | OpportunityContactRole_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | EndDate | End Date | DateTime | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | FiscalYearSettingsId | Fiscal Year Settings ID | Text | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | FullyQualifiedLabel | Fully Qualified Label | Text | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | Id | Period ID | Text | Yes | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | IsForecastPeriod | Is Forecast Period | Text | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| Period_Home | Period_Home__dll | Number | Number | Number | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | PeriodLabel | Period Name | Text | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | QuarterLabel | Quarter Name | Text | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | StartDate | Start Date | DateTime | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| Period_Home | Period_Home__dll | Type | Type | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | Description | Description | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | Id | Price Book ID | Text | Yes | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | IsActive | Active | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | IsArchived | Archived | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | IsStandard | Is Standard Price Book | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| Pricebook2_Home | Pricebook2_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | LastReferencedDate | Last Referenced Date | DateTime | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | LastViewedDate | Last Viewed Date | DateTime | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | Name | Price Book Name | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| Pricebook2_Home | Pricebook2_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | Id | Price Book Entry ID | Text | Yes | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | IsActive | Active | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | IsArchived | Archived | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| PricebookEntry_Home | PricebookEntry_Home__dll |  | KQ_Pricebook2Id | Text | No | SalesforceDotCom | Yes |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | Name | Product Name | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | Pricebook2Id | Price Book ID | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | Product2Id | Product ID | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | ProductCode | Product Code | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | UnitPrice | List Price | Number | No | SalesforceDotCom |  |  |
| PricebookEntry_Home | PricebookEntry_Home__dll | UseStandardPrice | Use Standard Price | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | CatalogId | Catalog ID | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | Description | Description | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | Id | Category ID | Text | Yes | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | IsNavigational | Show In Menu | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| ProductCategory_Home | ProductCategory_Home__dll |  | KQ_ParentCategoryId | Text | No | SalesforceDotCom | Yes |  |
| ProductCategory_Home | ProductCategory_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | LastReferencedDate | Last Referenced Date | DateTime | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | LastViewedDate | Last Viewed Date | DateTime | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | Name | Name | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | NumberOfProducts | Number of Products | Number | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | ParentCategoryId | Category ID | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | SortOrder | Sort Order | Number | No | SalesforceDotCom |  |  |
| ProductCategory_Home | ProductCategory_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | AreQualItemsExclFromDiscounts | Exclude qualifying items from discounts | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | CampaignId | Campaign ID | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll |  | cdp_sys_SourceVersion | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | CreatedById | Created By ID | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | CreatedDate | Created Date | DateTime | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll |  | Data Source | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll |  | Data Source Object | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | Description | Description | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | DiscountOrder | Discount Order | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | DiscountRestriction | Discount Restriction | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | DisplayName | Display Name | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | EndDateTime | End Datetime | DateTime | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | ExclusivityType | Exclusivity Type | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | Id | Promotion ID | Text | Yes | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | IsActive | Active | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | IsApproachingDiscountApplicable | Approaching Discount | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | IsAutomatic | Automatic | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | IsCommercePromotion | Commerce Promotion | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | IsDeleted | Deleted | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | IsQualCriteriaNotRequiredPerApplication | Qualifying Criteria Not Required Per App | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | IsTiered | Tiered Promotion | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll |  | KQ_CampaignId | Text | No | SalesforceDotCom | Yes |  |
| Promotion_Home | Promotion_Home__dll |  | KQ_Id | Text | No | SalesforceDotCom | Yes |  |
| Promotion_Home | Promotion_Home__dll | LastModifiedById | Last Modified By ID | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | LastModifiedDate | Last Modified Date | DateTime | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | LastReferencedDate | Last Referenced Date | DateTime | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | LastViewedDate | Last Viewed Date | DateTime | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | MaximumUsageCount | Maximum Applications Per Cart | Number | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | Name | Name | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | Objective | Objective | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | OwnerId | Owner ID | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | PriorityNumber | Priority Number | Number | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | QualifierCriteria | Qualifier Criteria | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | SfdcOrganizationId | SfdcOrganizationId | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | StartDateTime | Start Datetime | DateTime | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | SystemModstamp | System Modstamp | DateTime | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | TargetCriteria | Target Criteria | Text | No | SalesforceDotCom |  |  |
| Promotion_Home | Promotion_Home__dll | TermsAndConditions | Terms and Conditions | Text | No | SalesforceDotCom |  |  |

## DLO → DMO Field Mappings

Field-level mappings from Data Lake Objects to Data Model Objects, grouped by source → target pairing. Labels are taken from the mapping payload and the joined DLO field metadata; an API name shown as a label means no human label was available. **Business Label** and **Manual Mapping** are curated columns and are intentionally blank here.

### Account_Home (`Account_Home__dll`) → Account (`ssot__Account__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Account_Home__dll | Account_Home | AccountNumber__c | Account Number | ssot__Account__dlm | Account | ssot__Number__c | ssot__Number__c |  |  |  |
| Account_Home__dll | Account_Home | AccountSource__c | Account Source | ssot__Account__dlm | Account | ssot__AccountSource__c | ssot__AccountSource__c |  |  |  |
| Account_Home__dll | Account_Home | AnnualRevenue__c | Annual Revenue | ssot__Account__dlm | Account | ssot__AnnualRevenueAmount__c | ssot__AnnualRevenueAmount__c |  |  |  |
| Account_Home__dll | Account_Home | CreatedDate__c | Created Date | ssot__Account__dlm | Account | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| Account_Home__dll | Account_Home | DataSource__c | Data Source | ssot__Account__dlm | Account | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Account_Home__dll | Account_Home | DataSourceObject__c | Data Source Object | ssot__Account__dlm | Account | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Account_Home__dll | Account_Home | Description__c | Account Description | ssot__Account__dlm | Account | ssot__Description__c | ssot__Description__c |  |  |  |
| Account_Home__dll | Account_Home | Fax__c | Account Fax | ssot__Account__dlm | Account | ssot__FaxPhoneId__c | ssot__FaxPhoneId__c |  |  |  |
| Account_Home__dll | Account_Home | Id__c | Account ID | ssot__Account__dlm | Account | ssot__Id__c | ssot__Id__c |  |  |  |
| Account_Home__dll | Account_Home | Id__c | Account ID | ssot__Account__dlm | Account | ssot__SalesPhoneId__c | ssot__SalesPhoneId__c |  |  |  |
| Account_Home__dll | Account_Home | Id__c | Account ID | ssot__Account__dlm | Account | ssot__BillContactAddressId__c | ssot__BillContactAddressId__c |  |  |  |
| Account_Home__dll | Account_Home | Industry__c | Industry | ssot__Account__dlm | Account | ssot__PrimaryIndustry__c | ssot__PrimaryIndustry__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Fax__c | KQ_Fax | ssot__Account__dlm | Account | KQ_FaxPhoneId__c | KQ_FaxPhoneId__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Id__c | KQ_Id | ssot__Account__dlm | Account | KQ_Id__c | KQ_Id__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Id__c | KQ_Id | ssot__Account__dlm | Account | KQ_BillContactAddressId__c | KQ_BillContactAddressId__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Id__c | KQ_Id | ssot__Account__dlm | Account | KQ_SalesPhoneId__c | KQ_SalesPhoneId__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_ParentId__c | KQ_ParentId | ssot__Account__dlm | Account | KQ_ParentAccountId__c | KQ_ParentAccountId__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Phone__c | KQ_Phone | ssot__Account__dlm | Account | KQ_ShippingPhoneid__c | KQ_ShippingPhoneid__c |  |  |  |
| Account_Home__dll | Account_Home | LastActivityDate__c | Last Activity | ssot__Account__dlm | Account | ssot__LastActivityDate__c | ssot__LastActivityDate__c |  |  |  |
| Account_Home__dll | Account_Home | LastModifiedDate__c | Last Modified Date | ssot__Account__dlm | Account | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| Account_Home__dll | Account_Home | Name__c | Account Name | ssot__Account__dlm | Account | ssot__Name__c | ssot__Name__c |  |  |  |
| Account_Home__dll | Account_Home | NumberOfEmployees__c | Employees | ssot__Account__dlm | Account | ssot__EmployeeCount__c | ssot__EmployeeCount__c |  |  |  |
| Account_Home__dll | Account_Home | OwnerId__c | Owner ID | ssot__Account__dlm | Account | ssot__OwnerId__c | ssot__OwnerId__c |  |  |  |
| Account_Home__dll | Account_Home | Ownership__c | Ownership | ssot__Account__dlm | Account | ssot__AccountOwnershipType__c | ssot__AccountOwnershipType__c |  |  |  |
| Account_Home__dll | Account_Home | ParentId__c | Parent Account ID | ssot__Account__dlm | Account | ssot__ParentAccountId__c | ssot__ParentAccountId__c |  |  |  |
| Account_Home__dll | Account_Home | Phone__c | Account Phone | ssot__Account__dlm | Account | ssot__ShippingPhoneid__c | ssot__ShippingPhoneid__c |  |  |  |
| Account_Home__dll | Account_Home | PhotoUrl__c | Photo URL | ssot__Account__dlm | Account | ssot__ProfileImageUrl__c | ssot__ProfileImageUrl__c |  |  |  |
| Account_Home__dll | Account_Home | Rating__c | Account Rating | ssot__Account__dlm | Account | ssot__AccountRatingType__c | ssot__AccountRatingType__c |  |  |  |
| Account_Home__dll | Account_Home | Type__c | Account Type | ssot__Account__dlm | Account | ssot__AccountBusinessType__c | ssot__AccountBusinessType__c |  |  |  |
| Account_Home__dll | Account_Home | Type__c | Account Type | ssot__Account__dlm | Account | ssot__AccountType__c | ssot__AccountType__c |  |  |  |
| Account_Home__dll | Account_Home | Type__c | Account Type | ssot__Account__dlm | Account | ssot__AccountTypeId__c | ssot__AccountTypeId__c |  |  |  |
| Account_Home__dll | Account_Home | Website__c | Website | ssot__Account__dlm | Account | ssot__WebsiteAddr__c | ssot__WebsiteAddr__c |  |  |  |
| Account_Home__dll | Account_Home | Website__c | Website | ssot__Account__dlm | Account | ssot__AccountWebsiteURL__c | ssot__AccountWebsiteURL__c |  |  |  |

### Account_Home (`Account_Home__dll`) → Contact Point Address (`ssot__ContactPointAddress__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Account_Home__dll | Account_Home | BillingCity__c | Billing City | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__CityId__c | ssot__CityId__c |  |  |  |
| Account_Home__dll | Account_Home | BillingCountry__c | Billing Country | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__CountryName__c | ssot__CountryName__c |  |  |  |
| Account_Home__dll | Account_Home | BillingCountry__c | Billing Country | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__CountryId__c | ssot__CountryId__c |  |  |  |
| Account_Home__dll | Account_Home | BillingLatitude__c | Billing Latitude | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__GeoLatitude__c | ssot__GeoLatitude__c |  |  |  |
| Account_Home__dll | Account_Home | BillingLongitude__c | Billing Longitude | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__GeoLongitude__c | ssot__GeoLongitude__c |  |  |  |
| Account_Home__dll | Account_Home | BillingPostalCode__c | Billing Zip/Postal Code | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__PostalCodeId__c | ssot__PostalCodeId__c |  |  |  |
| Account_Home__dll | Account_Home | BillingState__c | Billing State/Province | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__StateProvinceName__c | ssot__StateProvinceName__c |  |  |  |
| Account_Home__dll | Account_Home | BillingState__c | Billing State/Province | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__StateProvinceId__c | ssot__StateProvinceId__c |  |  |  |
| Account_Home__dll | Account_Home | BillingStreet__c | Billing Street | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__AddressLine1__c | ssot__AddressLine1__c |  |  |  |
| Account_Home__dll | Account_Home | CreatedDate__c | Created Date | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| Account_Home__dll | Account_Home | DataSource__c | Data Source | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Account_Home__dll | Account_Home | DataSourceObject__c | Data Source Object | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Account_Home__dll | Account_Home | Id__c | Account ID | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__Id__c | ssot__Id__c |  |  |  |
| Account_Home__dll | Account_Home | Id__c | Account ID | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__PartyId__c | ssot__PartyId__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Id__c | KQ_Id | ssot__ContactPointAddress__dlm | Contact Point Address | KQ_Id__c | KQ_Id__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Id__c | KQ_Id | ssot__ContactPointAddress__dlm | Contact Point Address | KQ_PartyId__c | KQ_PartyId__c |  |  |  |
| Account_Home__dll | Account_Home | LastModifiedDate__c | Last Modified Date | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |

### Account_Home (`Account_Home__dll`) → Contact Point Phone (`ssot__ContactPointPhone__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Account_Home__dll | Account_Home | CreatedDate__c | Created Date | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| Account_Home__dll | Account_Home | DataSource__c | Data Source | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Account_Home__dll | Account_Home | DataSourceObject__c | Data Source Object | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Account_Home__dll | Account_Home | Id__c | Account ID | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__Id__c | ssot__Id__c |  |  |  |
| Account_Home__dll | Account_Home | Id__c | Account ID | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__PartyId__c | ssot__PartyId__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Id__c | KQ_Id | ssot__ContactPointPhone__dlm | Contact Point Phone | KQ_Id__c | KQ_Id__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Id__c | KQ_Id | ssot__ContactPointPhone__dlm | Contact Point Phone | KQ_PartyId__c | KQ_PartyId__c |  |  |  |
| Account_Home__dll | Account_Home | LastModifiedDate__c | Last Modified Date | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| Account_Home__dll | Account_Home | Phone__c | Account Phone | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__FormattedE164PhoneNumber__c | ssot__FormattedE164PhoneNumber__c |  |  |  |
| Account_Home__dll | Account_Home | Phone__c | Account Phone | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__TelephoneNumber__c | ssot__TelephoneNumber__c |  |  |  |

### Account_Home (`Account_Home__dll`) → Financial Customer (`ssot__FinancialCustomer__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Account_Home__dll | Account_Home | DataSource__c | Data Source | ssot__FinancialCustomer__dlm | Financial Customer | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Account_Home__dll | Account_Home | DataSourceObject__c | Data Source Object | ssot__FinancialCustomer__dlm | Financial Customer | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Account_Home__dll | Account_Home | Id__c | Account ID | ssot__FinancialCustomer__dlm | Financial Customer | ssot__AccountId__c | ssot__AccountId__c |  |  |  |
| Account_Home__dll | Account_Home | Id__c | Account ID | ssot__FinancialCustomer__dlm | Financial Customer | ssot__Id__c | ssot__Id__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Id__c | KQ_Id | ssot__FinancialCustomer__dlm | Financial Customer | KQ_Id__c | KQ_Id__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Id__c | KQ_Id | ssot__FinancialCustomer__dlm | Financial Customer | KQ_AccountId__c | KQ_AccountId__c |  |  |  |
| Account_Home__dll | Account_Home | Rating__c | Account Rating | ssot__FinancialCustomer__dlm | Financial Customer | ssot__CustomerRating__c | ssot__CustomerRating__c |  |  |  |

### Account_Home (`Account_Home__dll`) → Party (`ssot__Party__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Account_Home__dll | Account_Home | DataSource__c | Data Source | ssot__Party__dlm | Party | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Account_Home__dll | Account_Home | DataSourceObject__c | Data Source Object | ssot__Party__dlm | Party | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Account_Home__dll | Account_Home | Id__c | Account ID | ssot__Party__dlm | Party | ssot__Id__c | ssot__Id__c |  |  |  |
| Account_Home__dll | Account_Home | KQ_Id__c | KQ_Id | ssot__Party__dlm | Party | KQ_Id__c | KQ_Id__c |  |  |  |
| Account_Home__dll | Account_Home | Type__c | Account Type | ssot__Party__dlm | Party | ssot__PartyType__c | ssot__PartyType__c |  |  |  |

### BusinessHours_Home (`BusinessHours_Home__dll`) → Operating Hours (`ssot__OperatingHours__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BusinessHours_Home__dll | BusinessHours_Home | DataSource__c | Data Source | ssot__OperatingHours__dlm | Operating Hours | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | DataSourceObject__c | Data Source Object | ssot__OperatingHours__dlm | Operating Hours | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | FridayEndTime__c | Friday End | ssot__OperatingHours__dlm | Operating Hours | ssot__Friday_EndTime__c | ssot__Friday_EndTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | FridayStartTime__c | Friday Start | ssot__OperatingHours__dlm | Operating Hours | ssot__Friday_StartTime__c | ssot__Friday_StartTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | Id__c | Business Hours ID | ssot__OperatingHours__dlm | Operating Hours | ssot__Id__c | ssot__Id__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | IsActive__c | Active | ssot__OperatingHours__dlm | Operating Hours | ssot__isActive__c | ssot__isActive__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | IsDefault__c | Default Business Hours | ssot__OperatingHours__dlm | Operating Hours | ssot__isDefault__c | ssot__isDefault__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | KQ_Id__c | KQ_Id | ssot__OperatingHours__dlm | Operating Hours | KQ_Id__c | KQ_Id__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | MondayEndTime__c | Monday End | ssot__OperatingHours__dlm | Operating Hours | ssot__Monday_EndTime__c | ssot__Monday_EndTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | MondayStartTime__c | Monday Start | ssot__OperatingHours__dlm | Operating Hours | ssot__Monday_StartTime__c | ssot__Monday_StartTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | Name__c | Business Hours Name | ssot__OperatingHours__dlm | Operating Hours | ssot__Name__c | ssot__Name__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | SaturdayEndTime__c | Saturday End | ssot__OperatingHours__dlm | Operating Hours | ssot__Saturday_EndTime__c | ssot__Saturday_EndTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | SaturdayStartTime__c | Saturday Start | ssot__OperatingHours__dlm | Operating Hours | ssot__Saturday_StartTime__c | ssot__Saturday_StartTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | SundayEndTime__c | Sunday End | ssot__OperatingHours__dlm | Operating Hours | ssot__Sunday_EndTime__c | ssot__Sunday_EndTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | SundayStartTime__c | Sunday Start | ssot__OperatingHours__dlm | Operating Hours | ssot__Sunday_StartTime__c | ssot__Sunday_StartTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | ThursdayEndTime__c | Thursday End | ssot__OperatingHours__dlm | Operating Hours | ssot__Thursday_EndTime__c | ssot__Thursday_EndTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | ThursdayStartTime__c | Thursday Start | ssot__OperatingHours__dlm | Operating Hours | ssot__Thursday_StartTime__c | ssot__Thursday_StartTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | TimeZoneSidKey__c | Time Zone | ssot__OperatingHours__dlm | Operating Hours | ssot__TimeZone__c | ssot__TimeZone__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | TuesdayEndTime__c | Tuesday End | ssot__OperatingHours__dlm | Operating Hours | ssot__Tuesday_EndTime__c | ssot__Tuesday_EndTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | TuesdayStartTime__c | Tuesday Start | ssot__OperatingHours__dlm | Operating Hours | ssot__Tuesday_StartTime__c | ssot__Tuesday_StartTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | WednesdayEndTime__c | Wednesday End | ssot__OperatingHours__dlm | Operating Hours | ssot__Wednesday_EndTime__c | ssot__Wednesday_EndTime__c |  |  |  |
| BusinessHours_Home__dll | BusinessHours_Home | WednesdayStartTime__c | Wednesday Start | ssot__OperatingHours__dlm | Operating Hours | ssot__Wednesday_StartTime__c | ssot__Wednesday_StartTime__c |  |  |  |

### Campaign_Home (`Campaign_Home__dll`) → Campaign (`ssot__Campaign__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Campaign_Home__dll | Campaign_Home | ActualCost__c | Actual Cost in Campaign | ssot__Campaign__dlm | Campaign | ssot__ActualCostAmount__c | ssot__ActualCostAmount__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | BudgetedCost__c | Budgeted Cost in Campaign | ssot__Campaign__dlm | Campaign | ssot__BudgetedCostAmount__c | ssot__BudgetedCostAmount__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | DataSource__c | Data Source | ssot__Campaign__dlm | Campaign | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | DataSourceObject__c | Data Source Object | ssot__Campaign__dlm | Campaign | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | Description__c | Description | ssot__Campaign__dlm | Campaign | ssot__Description__c | ssot__Description__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | EndDate__c | End Date | ssot__Campaign__dlm | Campaign | ssot__CampaignEndDate__c | ssot__CampaignEndDate__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | ExpectedResponse__c | Expected Response (%) | ssot__Campaign__dlm | Campaign | ssot__ExpectedResponsePercent__c | ssot__ExpectedResponsePercent__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | ExpectedRevenue__c | Expected Revenue in Campaign | ssot__Campaign__dlm | Campaign | ssot__ExpectedRevenueAmount__c | ssot__ExpectedRevenueAmount__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | Id__c | Campaign ID | ssot__Campaign__dlm | Campaign | ssot__ParentCampaignId__c | ssot__ParentCampaignId__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | Id__c | Campaign ID | ssot__Campaign__dlm | Campaign | ssot__Id__c | ssot__Id__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | KQ_Id__c | KQ_Id | ssot__Campaign__dlm | Campaign | KQ_Id__c | KQ_Id__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | KQ_Id__c | KQ_Id | ssot__Campaign__dlm | Campaign | KQ_ParentCampaignId__c | KQ_ParentCampaignId__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | Name__c | Name | ssot__Campaign__dlm | Campaign | ssot__Name__c | ssot__Name__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | StartDate__c | Start Date | ssot__Campaign__dlm | Campaign | ssot__CampaignStartDate__c | ssot__CampaignStartDate__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | Status__c | Status | ssot__Campaign__dlm | Campaign | ssot__CampaignStatus__c | ssot__CampaignStatus__c |  |  |  |
| Campaign_Home__dll | Campaign_Home | Type__c | Type | ssot__Campaign__dlm | Campaign | ssot__CampaignType__c | ssot__CampaignType__c |  |  |  |

### Contact_Home (`Contact_Home__dll`) → Account Contact (`ssot__AccountContact__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contact_Home__dll | Contact_Home | AccountId__c | Account ID | ssot__AccountContact__dlm | Account Contact | ssot__AccountId__c | ssot__AccountId__c |  |  |  |
| Contact_Home__dll | Contact_Home | AssistantName__c | Assistant&#39;s Name | ssot__AccountContact__dlm | Account Contact | ssot__AssistantName__c | ssot__AssistantName__c |  |  |  |
| Contact_Home__dll | Contact_Home | AssistantPhone__c | Asst. Phone | ssot__AccountContact__dlm | Account Contact | ssot__AssistantPhone__c | ssot__AssistantPhone__c |  |  |  |
| Contact_Home__dll | Contact_Home | CreatedDate__c | Created Date | ssot__AccountContact__dlm | Account Contact | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSource__c | Data Source | ssot__AccountContact__dlm | Account Contact | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSourceObject__c | Data Source Object | ssot__AccountContact__dlm | Account Contact | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Department__c | Department | ssot__AccountContact__dlm | Account Contact | ssot__DepartmentName__c | ssot__DepartmentName__c |  |  |  |
| Contact_Home__dll | Contact_Home | Fax__c | Business Fax | ssot__AccountContact__dlm | Account Contact | ssot__FaxPhoneId__c | ssot__FaxPhoneId__c |  |  |  |
| Contact_Home__dll | Contact_Home | FirstName__c | First Name | ssot__AccountContact__dlm | Account Contact | ssot__FirstName__c | ssot__FirstName__c |  |  |  |
| Contact_Home__dll | Contact_Home | GenderIdentity__c | Gender Identity | ssot__AccountContact__dlm | Account Contact | ssot__Gender__c | ssot__Gender__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__AccountContact__dlm | Account Contact | ssot__HomePhoneId__c | ssot__HomePhoneId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__AccountContact__dlm | Account Contact | ssot__ContactEmailId__c | ssot__ContactEmailId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__AccountContact__dlm | Account Contact | ssot__MailingAddressId__c | ssot__MailingAddressId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__AccountContact__dlm | Account Contact | ssot__BusinessPhoneId__c | ssot__BusinessPhoneId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__AccountContact__dlm | Account Contact | ssot__Id__c | ssot__Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__AccountContact__dlm | Account Contact | ssot__IndividualId__c | ssot__IndividualId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__AccountContact__dlm | Account Contact | ssot__MobilePhoneId__c | ssot__MobilePhoneId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_AccountId__c | KQ_AccountId | ssot__AccountContact__dlm | Account Contact | KQ_AccountId__c | KQ_AccountId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Fax__c | KQ_Fax | ssot__AccountContact__dlm | Account Contact | KQ_FaxPhoneId__c | KQ_FaxPhoneId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__AccountContact__dlm | Account Contact | KQ_Id__c | KQ_Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__AccountContact__dlm | Account Contact | KQ_BusinessPhoneId__c | KQ_BusinessPhoneId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__AccountContact__dlm | Account Contact | KQ_ContactEmailId__c | KQ_ContactEmailId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__AccountContact__dlm | Account Contact | KQ_HomePhoneId__c | KQ_HomePhoneId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__AccountContact__dlm | Account Contact | KQ_IndividualId__c | KQ_IndividualId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__AccountContact__dlm | Account Contact | KQ_MailingAddressId__c | KQ_MailingAddressId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__AccountContact__dlm | Account Contact | KQ_MobilePhoneId__c | KQ_MobilePhoneId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_ReportsToId__c | KQ_ReportsToId | ssot__AccountContact__dlm | Account Contact | KQ_ReportsToAccountContactId__c | KQ_ReportsToAccountContactId__c |  |  |  |
| Contact_Home__dll | Contact_Home | LastActivityDate__c | Last Activity | ssot__AccountContact__dlm | Account Contact | ssot__LastActivityDate__c | ssot__LastActivityDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | LastModifiedDate__c | Last Modified Date | ssot__AccountContact__dlm | Account Contact | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | LastName__c | Last Name | ssot__AccountContact__dlm | Account Contact | ssot__LastName__c | ssot__LastName__c |  |  |  |
| Contact_Home__dll | Contact_Home | Name__c | Full Name | ssot__AccountContact__dlm | Account Contact | ssot__PersonName__c | ssot__PersonName__c |  |  |  |
| Contact_Home__dll | Contact_Home | OwnerId__c | Owner ID | ssot__AccountContact__dlm | Account Contact | ssot__OwnerId__c | ssot__OwnerId__c |  |  |  |
| Contact_Home__dll | Contact_Home | ReportsToId__c | Reports To ID | ssot__AccountContact__dlm | Account Contact | ssot__ReportsToAccountContactId__c | ssot__ReportsToAccountContactId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Title__c | Title | ssot__AccountContact__dlm | Account Contact | ssot__Title__c | ssot__Title__c |  |  |  |

### Contact_Home (`Contact_Home__dll`) → Contact Point Address (`ssot__ContactPointAddress__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contact_Home__dll | Contact_Home | CreatedDate__c | Created Date | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSource__c | Data Source | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSourceObject__c | Data Source Object | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__Id__c | ssot__Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__PartyId__c | ssot__PartyId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__ContactPointAddress__dlm | Contact Point Address | KQ_Id__c | KQ_Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__ContactPointAddress__dlm | Contact Point Address | KQ_PartyId__c | KQ_PartyId__c |  |  |  |
| Contact_Home__dll | Contact_Home | LastModifiedDate__c | Last Modified Date | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingCity__c | Mailing City | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__CityId__c | ssot__CityId__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingCity__c | Mailing City | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__CityName__c | ssot__CityName__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingCountry__c | Mailing Country | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__CountryName__c | ssot__CountryName__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingCountry__c | Mailing Country | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__CountryId__c | ssot__CountryId__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingLatitude__c | Mailing Latitude | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__GeoLatitude__c | ssot__GeoLatitude__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingLongitude__c | Mailing Longitude | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__GeoLongitude__c | ssot__GeoLongitude__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingPostalCode__c | Mailing Zip/Postal Code | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__PostalCodeText__c | ssot__PostalCodeText__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingPostalCode__c | Mailing Zip/Postal Code | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__PostalCodeId__c | ssot__PostalCodeId__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingState__c | Mailing State/Province | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__StateProvinceName__c | ssot__StateProvinceName__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingState__c | Mailing State/Province | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__StateProvinceId__c | ssot__StateProvinceId__c |  |  |  |
| Contact_Home__dll | Contact_Home | MailingStreet__c | Mailing Street | ssot__ContactPointAddress__dlm | Contact Point Address | ssot__AddressLine1__c | ssot__AddressLine1__c |  |  |  |

### Contact_Home (`Contact_Home__dll`) → Contact Point Email (`ssot__ContactPointEmail__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contact_Home__dll | Contact_Home | CreatedDate__c | Created Date | ssot__ContactPointEmail__dlm | Contact Point Email | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSource__c | Data Source | ssot__ContactPointEmail__dlm | Contact Point Email | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSourceObject__c | Data Source Object | ssot__ContactPointEmail__dlm | Contact Point Email | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Email__c | Email | ssot__ContactPointEmail__dlm | Contact Point Email | ssot__EmailAddress__c | ssot__EmailAddress__c |  |  |  |
| Contact_Home__dll | Contact_Home | EmailBouncedDate__c | Email Bounced Date | ssot__ContactPointEmail__dlm | Contact Point Email | ssot__EmailLatestBounceDateTime__c | ssot__EmailLatestBounceDateTime__c |  |  |  |
| Contact_Home__dll | Contact_Home | EmailBouncedReason__c | Email Bounced Reason | ssot__ContactPointEmail__dlm | Contact Point Email | ssot__EmailLatestBounceReasonText__c | ssot__EmailLatestBounceReasonText__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__ContactPointEmail__dlm | Contact Point Email | ssot__Id__c | ssot__Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__ContactPointEmail__dlm | Contact Point Email | ssot__PartyId__c | ssot__PartyId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__ContactPointEmail__dlm | Contact Point Email | KQ_Id__c | KQ_Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__ContactPointEmail__dlm | Contact Point Email | KQ_PartyId__c | KQ_PartyId__c |  |  |  |
| Contact_Home__dll | Contact_Home | LastModifiedDate__c | Last Modified Date | ssot__ContactPointEmail__dlm | Contact Point Email | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |

### Contact_Home (`Contact_Home__dll`) → Contact Point Phone (`ssot__ContactPointPhone__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contact_Home__dll | Contact_Home | CreatedDate__c | Created Date | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSource__c | Data Source | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSourceObject__c | Data Source Object | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__Id__c | ssot__Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__PartyId__c | ssot__PartyId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__ContactPointPhone__dlm | Contact Point Phone | KQ_Id__c | KQ_Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__ContactPointPhone__dlm | Contact Point Phone | KQ_PartyId__c | KQ_PartyId__c |  |  |  |
| Contact_Home__dll | Contact_Home | LastModifiedDate__c | Last Modified Date | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | MobilePhone__c | Mobile Phone | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__ForPersonalUse__c | ssot__ForPersonalUse__c |  |  |  |
| Contact_Home__dll | Contact_Home | Phone__c | Business Phone | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__ForBusinessUse__c | ssot__ForBusinessUse__c |  |  |  |
| Contact_Home__dll | Contact_Home | Phone__c | Business Phone | ssot__ContactPointPhone__dlm | Contact Point Phone | ssot__TelephoneNumber__c | ssot__TelephoneNumber__c |  |  |  |

### Contact_Home (`Contact_Home__dll`) → Individual (`ssot__Individual__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contact_Home__dll | Contact_Home | AccountId__c | Account ID | ssot__Individual__dlm | Individual | ssot__PrimaryAccountId__c | ssot__PrimaryAccountId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Birthdate__c | Birthdate | ssot__Individual__dlm | Individual | ssot__BirthDate__c | ssot__BirthDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | CreatedDate__c | Created Date | ssot__Individual__dlm | Individual | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSource__c | Data Source | ssot__Individual__dlm | Individual | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSourceObject__c | Data Source Object | ssot__Individual__dlm | Individual | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Contact_Home__dll | Contact_Home | FirstName__c | First Name | ssot__Individual__dlm | Individual | ssot__FirstName__c | ssot__FirstName__c |  |  |  |
| Contact_Home__dll | Contact_Home | GenderIdentity__c | Gender Identity | ssot__Individual__dlm | Individual | ssot__GenderIdentity__c | ssot__GenderIdentity__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__Individual__dlm | Individual | ssot__Id__c | ssot__Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__Individual__dlm | Individual | ssot__PartyId__c | ssot__PartyId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__Individual__dlm | Individual | ssot__ExternalRecordId__c | ssot__ExternalRecordId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_AccountId__c | KQ_AccountId | ssot__Individual__dlm | Individual | KQ_PrimaryAccountId__c | KQ_PrimaryAccountId__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__Individual__dlm | Individual | KQ_Id__c | KQ_Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__Individual__dlm | Individual | KQ_PartyId__c | KQ_PartyId__c |  |  |  |
| Contact_Home__dll | Contact_Home | LastModifiedDate__c | Last Modified Date | ssot__Individual__dlm | Individual | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| Contact_Home__dll | Contact_Home | LastName__c | Last Name | ssot__Individual__dlm | Individual | ssot__LastName__c | ssot__LastName__c |  |  |  |
| Contact_Home__dll | Contact_Home | Name__c | Full Name | ssot__Individual__dlm | Individual | ssot__PersonName__c | ssot__PersonName__c |  |  |  |
| Contact_Home__dll | Contact_Home | PhotoUrl__c | Photo URL | ssot__Individual__dlm | Individual | ssot__PhotoURL__c | ssot__PhotoURL__c |  |  |  |
| Contact_Home__dll | Contact_Home | Pronouns__c | Pronouns | ssot__Individual__dlm | Individual | ssot__Pronoun__c | ssot__Pronoun__c |  |  |  |
| Contact_Home__dll | Contact_Home | Salutation__c | Salutation | ssot__Individual__dlm | Individual | ssot__Salutation__c | ssot__Salutation__c |  |  |  |
| Contact_Home__dll | Contact_Home | SfdcOrganizationId__c | SfdcOrganizationId | ssot__Individual__dlm | Individual | ssot__ExternalSourceId__c | ssot__ExternalSourceId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Title__c | Title | ssot__Individual__dlm | Individual | ssot__TitleName__c | ssot__TitleName__c |  |  |  |

### Contact_Home (`Contact_Home__dll`) → Party (`ssot__Party__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contact_Home__dll | Contact_Home | DataSource__c | Data Source | ssot__Party__dlm | Party | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Contact_Home__dll | Contact_Home | DataSourceObject__c | Data Source Object | ssot__Party__dlm | Party | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__Party__dlm | Party | ssot__IndividualId__c | ssot__IndividualId__c |  |  |  |
| Contact_Home__dll | Contact_Home | Id__c | Contact ID | ssot__Party__dlm | Party | ssot__Id__c | ssot__Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__Party__dlm | Party | KQ_Id__c | KQ_Id__c |  |  |  |
| Contact_Home__dll | Contact_Home | KQ_Id__c | KQ_Id | ssot__Party__dlm | Party | KQ_IndividualId__c | KQ_IndividualId__c |  |  |  |

### DataCategory_Home (`DataCategory_Home__dll`) → Category (`ssot__Category__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DataCategory_Home__dll | DataCategory_Home | DataSource__c | Data Source | ssot__Category__dlm | Category | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| DataCategory_Home__dll | DataCategory_Home | DataSourceObject__c | Data Source Object | ssot__Category__dlm | Category | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| DataCategory_Home__dll | DataCategory_Home | DeveloperName__c | Developer Name | ssot__Category__dlm | Category | ssot__Name__c | ssot__Name__c |  |  |  |
| DataCategory_Home__dll | DataCategory_Home | Id__c | Data Category ID | ssot__Category__dlm | Category | ssot__Id__c | ssot__Id__c |  |  |  |
| DataCategory_Home__dll | DataCategory_Home | KQ_Id__c | KQ_Id | ssot__Category__dlm | Category | KQ_Id__c | KQ_Id__c |  |  |  |
| DataCategory_Home__dll | DataCategory_Home | MasterLabel__c | Label | ssot__Category__dlm | Category | ssot__LabelName__c | ssot__LabelName__c |  |  |  |
| DataCategory_Home__dll | DataCategory_Home | SortOrder__c | Sort Order | ssot__Category__dlm | Category | ssot__SortOrderNumber__c | ssot__SortOrderNumber__c |  |  |  |

### DataCategoryGroup_Home (`DataCategoryGroup_Home__dll`) → Category (`ssot__Category__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DataCategoryGroup_Home__dll | DataCategoryGroup_Home | DataSource__c | Data Source | ssot__Category__dlm | Category | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| DataCategoryGroup_Home__dll | DataCategoryGroup_Home | DataSourceObject__c | Data Source Object | ssot__Category__dlm | Category | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| DataCategoryGroup_Home__dll | DataCategoryGroup_Home | DeveloperName__c | Developer Name | ssot__Category__dlm | Category | ssot__Name__c | ssot__Name__c |  |  |  |
| DataCategoryGroup_Home__dll | DataCategoryGroup_Home | Id__c | Data Category Type ID | ssot__Category__dlm | Category | ssot__Id__c | ssot__Id__c |  |  |  |
| DataCategoryGroup_Home__dll | DataCategoryGroup_Home | KQ_Id__c | KQ_Id | ssot__Category__dlm | Category | KQ_Id__c | KQ_Id__c |  |  |  |
| DataCategoryGroup_Home__dll | DataCategoryGroup_Home | MasterLabel__c | Label | ssot__Category__dlm | Category | ssot__LabelName__c | ssot__LabelName__c |  |  |  |
| DataCategoryGroup_Home__dll | DataCategoryGroup_Home | Status__c | Status | ssot__Category__dlm | Category | ssot__CategoryStatus__c | ssot__CategoryStatus__c |  |  |  |

### EngagementChannelType_Home (`EngagementChannelType_Home__dll`) → Engagement Channel Type (`ssot__EngagementChannelType__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EngagementChannelType_Home__dll | EngagementChannelType_Home | ContactPointType__c | Contact Point Type | ssot__EngagementChannelType__dlm | Engagement Channel Type | ssot__ContactPointType__c | ssot__ContactPointType__c |  |  |  |
| EngagementChannelType_Home__dll | EngagementChannelType_Home | DataSource__c | Data Source | ssot__EngagementChannelType__dlm | Engagement Channel Type | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| EngagementChannelType_Home__dll | EngagementChannelType_Home | DataSourceObject__c | Data Source Object | ssot__EngagementChannelType__dlm | Engagement Channel Type | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| EngagementChannelType_Home__dll | EngagementChannelType_Home | Id__c | Engagement Channel Type ID | ssot__EngagementChannelType__dlm | Engagement Channel Type | ssot__Id__c | ssot__Id__c |  |  |  |
| EngagementChannelType_Home__dll | EngagementChannelType_Home | KQ_Id__c | KQ_Id | ssot__EngagementChannelType__dlm | Engagement Channel Type | KQ_Id__c | KQ_Id__c |  |  |  |
| EngagementChannelType_Home__dll | EngagementChannelType_Home | Name__c | Name | ssot__EngagementChannelType__dlm | Engagement Channel Type | ssot__Name__c | ssot__Name__c |  |  |  |
| EngagementChannelType_Home__dll | EngagementChannelType_Home | UsageType__c | Usage Type | ssot__EngagementChannelType__dlm | Engagement Channel Type | UsageType__c | UsageType__c |  |  |  |

### ListEmail_Home (`ListEmail_Home__dll`) → Bulk Email Message (`ssot__BulkEmailMessage__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ListEmail_Home__dll | ListEmail_Home | CampaignId__c | Campaign ID | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__CampaignId__c | ssot__CampaignId__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | CcAddress__c | CC Address | ssot__BulkEmailMessage__dlm | Bulk Email Message | CcAddress__c | CcAddress__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | DataSource__c | Data Source | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | DataSourceObject__c | Data Source Object | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | FromAddress__c | From Address | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__FromAddress__c | ssot__FromAddress__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | FromName__c | From Name | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__FromName__c | ssot__FromName__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | HasAttachment__c | Has Attachment | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__HasAttachment__c | ssot__HasAttachment__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | HtmlBody__c | Html Body | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__HTMLBodyText__c | ssot__HTMLBodyText__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | Id__c | List Email ID | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__Id__c | ssot__Id__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | KQ_CampaignId__c | KQ_CampaignId | ssot__BulkEmailMessage__dlm | Bulk Email Message | KQ_CampaignId__c | KQ_CampaignId__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | KQ_Id__c | KQ_Id | ssot__BulkEmailMessage__dlm | Bulk Email Message | KQ_Id__c | KQ_Id__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | Name__c | Name | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__Name__c | ssot__Name__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | OwnerId__c | Owner ID | ssot__BulkEmailMessage__dlm | Bulk Email Message | OwnerId__c | OwnerId__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | ReplyToAddress__c | Reply To Address | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__ReplyToAddress__c | ssot__ReplyToAddress__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | ReplyToName__c | Reply To Name | ssot__BulkEmailMessage__dlm | Bulk Email Message | ReplyToName__c | ReplyToName__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | ScheduledDate__c | Scheduled Date | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__ScheduledDate__c | ssot__ScheduledDate__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | SentVia__c | Sent Via | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__SendMechanismName__c | ssot__SendMechanismName__c |  |  |  |
| ListEmail_Home__dll | ListEmail_Home | Subject__c | Subject | ssot__BulkEmailMessage__dlm | Bulk Email Message | ssot__Subject__c | ssot__Subject__c |  |  |  |

### ManagedContent_Home (`ManagedContent_Home__dll`) → Digital Content (`ssot__DigitalContent__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ManagedContent_Home__dll | ManagedContent_Home | ContentTypeFullyQualifiedName__c | Content Type Fully Qualified Name | ssot__DigitalContent__dlm | Digital Content | ssot__DigitalContentType__c | ssot__DigitalContentType__c |  |  |  |
| ManagedContent_Home__dll | ManagedContent_Home | DataSource__c | Data Source | ssot__DigitalContent__dlm | Digital Content | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| ManagedContent_Home__dll | ManagedContent_Home | DataSourceObject__c | Data Source Object | ssot__DigitalContent__dlm | Digital Content | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| ManagedContent_Home__dll | ManagedContent_Home | Id__c | Managed Content ID | ssot__DigitalContent__dlm | Digital Content | ssot__Id__c | ssot__Id__c |  |  |  |
| ManagedContent_Home__dll | ManagedContent_Home | KQ_Id__c | KQ_Id | ssot__DigitalContent__dlm | Digital Content | KQ_Id__c | KQ_Id__c |  |  |  |
| ManagedContent_Home__dll | ManagedContent_Home | Name__c | Name | ssot__DigitalContent__dlm | Digital Content | ssot__Name__c | ssot__Name__c |  |  |  |

### MarketSegment_Home (`MarketSegment_Home__dll`) → Market Segment (`ssot__MarketSegment__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MarketSegment_Home__dll | MarketSegment_Home | CreatedDate__c | Created Date | ssot__MarketSegment__dlm | Market Segment | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | DataSource__c | Data Source | ssot__MarketSegment__dlm | Market Segment | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | DataSourceObject__c | Data Source Object | ssot__MarketSegment__dlm | Market Segment | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | Description__c | Segment Description | ssot__MarketSegment__dlm | Market Segment | ssot__Description__c | ssot__Description__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | ExcludeCriteria__c | Exclude Criteria | ssot__MarketSegment__dlm | Market Segment | ssot__ExcludeCriteriaText__c | ssot__ExcludeCriteriaText__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | Id__c | Segment ID | ssot__MarketSegment__dlm | Market Segment | ssot__Id__c | ssot__Id__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | IncludeCriteria__c | Include Criteria | ssot__MarketSegment__dlm | Market Segment | ssot__IncludeCriteriaText__c | ssot__IncludeCriteriaText__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | KQ_Id__c | KQ_Id | ssot__MarketSegment__dlm | Market Segment | KQ_Id__c | KQ_Id__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | LastModifiedDate__c | Last Modified Date | ssot__MarketSegment__dlm | Market Segment | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | LastPublishStatusDateTime__c | Last Publish Status Date Time | ssot__MarketSegment__dlm | Market Segment | ssot__LastStatusDate__c | ssot__LastStatusDate__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | LastSegmentStatusErrorDetails__c | Segment Status Error Details | ssot__MarketSegment__dlm | Market Segment | ssot__LastStatusErrorMessageText__c | ssot__LastStatusErrorMessageText__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | Name__c | Segment Name | ssot__MarketSegment__dlm | Market Segment | ssot__Name__c | ssot__Name__c |  |  |  |
| MarketSegment_Home__dll | MarketSegment_Home | PublishStatus__c | Publish Status | ssot__MarketSegment__dlm | Market Segment | ssot__MktSegPubStatus__c | ssot__MktSegPubStatus__c |  |  |  |

### OpportunityContactRole_Home (`OpportunityContactRole_Home__dll`) → Opportunity Contact (`ssot__OpportunityContact__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OpportunityContactRole_Home__dll | OpportunityContactRole_Home | ContactId__c | Contact ID | ssot__OpportunityContact__dlm | Opportunity Contact | ssot__AccountContactId__c | ssot__AccountContactId__c |  |  |  |
| OpportunityContactRole_Home__dll | OpportunityContactRole_Home | DataSource__c | Data Source | ssot__OpportunityContact__dlm | Opportunity Contact | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| OpportunityContactRole_Home__dll | OpportunityContactRole_Home | DataSourceObject__c | Data Source Object | ssot__OpportunityContact__dlm | Opportunity Contact | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| OpportunityContactRole_Home__dll | OpportunityContactRole_Home | Id__c | Contact Role ID | ssot__OpportunityContact__dlm | Opportunity Contact | ssot__Id__c | ssot__Id__c |  |  |  |
| OpportunityContactRole_Home__dll | OpportunityContactRole_Home | IsPrimary__c | Primary | ssot__OpportunityContact__dlm | Opportunity Contact | ssot__IsPrimary__c | ssot__IsPrimary__c |  |  |  |
| OpportunityContactRole_Home__dll | OpportunityContactRole_Home | KQ_ContactId__c | KQ_ContactId | ssot__OpportunityContact__dlm | Opportunity Contact | KQ_AccountContactId__c | KQ_AccountContactId__c |  |  |  |
| OpportunityContactRole_Home__dll | OpportunityContactRole_Home | KQ_Id__c | KQ_Id | ssot__OpportunityContact__dlm | Opportunity Contact | KQ_Id__c | KQ_Id__c |  |  |  |
| OpportunityContactRole_Home__dll | OpportunityContactRole_Home | OpportunityId__c | Opportunity ID | ssot__OpportunityContact__dlm | Opportunity Contact | ssot__OpportunityId__c | ssot__OpportunityId__c |  |  |  |
| OpportunityContactRole_Home__dll | OpportunityContactRole_Home | Role__c | Role | ssot__OpportunityContact__dlm | Opportunity Contact | ssot__OpportunitytContactRole__c | ssot__OpportunitytContactRole__c |  |  |  |

### Period_Home (`Period_Home__dll`) → Business Period (`ssot__BusinessPeriod__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Period_Home__dll | Period_Home | DataSource__c | Data Source | ssot__BusinessPeriod__dlm | Business Period | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Period_Home__dll | Period_Home | DataSourceObject__c | Data Source Object | ssot__BusinessPeriod__dlm | Business Period | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Period_Home__dll | Period_Home | FullyQualifiedLabel__c | Fully Qualified Label | ssot__BusinessPeriod__dlm | Business Period | ssot__FullyQualifiedLabel__c | ssot__FullyQualifiedLabel__c |  |  |  |
| Period_Home__dll | Period_Home | Id__c | Period ID | ssot__BusinessPeriod__dlm | Business Period | ssot__Id__c | ssot__Id__c |  |  |  |
| Period_Home__dll | Period_Home | KQ_Id__c | KQ_Id | ssot__BusinessPeriod__dlm | Business Period | KQ_Id__c | KQ_Id__c |  |  |  |
| Period_Home__dll | Period_Home | Number__c | Number | ssot__BusinessPeriod__dlm | Business Period | ssot__PeriodNumber__c | ssot__PeriodNumber__c |  |  |  |
| Period_Home__dll | Period_Home | PeriodLabel__c | Period Name | ssot__BusinessPeriod__dlm | Business Period | ssot__PeriodLabel__c | ssot__PeriodLabel__c |  |  |  |
| Period_Home__dll | Period_Home | QuarterLabel__c | Quarter Name | ssot__BusinessPeriod__dlm | Business Period | ssot__QuarterLabel__c | ssot__QuarterLabel__c |  |  |  |
| Period_Home__dll | Period_Home | Type__c | Type | ssot__BusinessPeriod__dlm | Business Period | ssot__BusinessPeriodType__c | ssot__BusinessPeriodType__c |  |  |  |

### Pricebook2_Home (`Pricebook2_Home__dll`) → Price Book (`ssot__PriceBook__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pricebook2_Home__dll | Pricebook2_Home | DataSource__c | Data Source | ssot__PriceBook__dlm | Price Book | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Pricebook2_Home__dll | Pricebook2_Home | DataSourceObject__c | Data Source Object | ssot__PriceBook__dlm | Price Book | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Pricebook2_Home__dll | Pricebook2_Home | Description__c | Description | ssot__PriceBook__dlm | Price Book | ssot__Description__c | ssot__Description__c |  |  |  |
| Pricebook2_Home__dll | Pricebook2_Home | Id__c | Price Book ID | ssot__PriceBook__dlm | Price Book | ssot__Id__c | ssot__Id__c |  |  |  |
| Pricebook2_Home__dll | Pricebook2_Home | IsActive__c | Active | ssot__PriceBook__dlm | Price Book | ssot__IsActive__c | ssot__IsActive__c |  |  |  |
| Pricebook2_Home__dll | Pricebook2_Home | IsArchived__c | Archived | ssot__PriceBook__dlm | Price Book | ssot__IsArchived__c | ssot__IsArchived__c |  |  |  |
| Pricebook2_Home__dll | Pricebook2_Home | IsDeleted__c | Deleted | ssot__PriceBook__dlm | Price Book | ssot__IsDeleted__c | ssot__IsDeleted__c |  |  |  |
| Pricebook2_Home__dll | Pricebook2_Home | IsStandard__c | Is Standard Price Book | ssot__PriceBook__dlm | Price Book | ssot__IsStandardPriceBook__c | ssot__IsStandardPriceBook__c |  |  |  |
| Pricebook2_Home__dll | Pricebook2_Home | KQ_Id__c | KQ_Id | ssot__PriceBook__dlm | Price Book | KQ_Id__c | KQ_Id__c |  |  |  |
| Pricebook2_Home__dll | Pricebook2_Home | LastModifiedDate__c | Last Modified Date | ssot__PriceBook__dlm | Price Book | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| Pricebook2_Home__dll | Pricebook2_Home | Name__c | Price Book Name | ssot__PriceBook__dlm | Price Book | ssot__Name__c | ssot__Name__c |  |  |  |

### PricebookEntry_Home (`PricebookEntry_Home__dll`) → Price Book Entry (`ssot__PriceBookEntry__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PricebookEntry_Home__dll | PricebookEntry_Home | CreatedById__c | Created By ID | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__CreatedById__c | ssot__CreatedById__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | CreatedDate__c | Created Date | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | DataSource__c | Data Source | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | DataSourceObject__c | Data Source Object | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | Id__c | Price Book Entry ID | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__Id__c | ssot__Id__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | IsActive__c | Active | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__IsActive__c | ssot__IsActive__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | IsArchived__c | Archived | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__IsArchived__c | ssot__IsArchived__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | IsDeleted__c | Deleted | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__IsDeleted__c | ssot__IsDeleted__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | KQ_Id__c | KQ_Id | ssot__PriceBookEntry__dlm | Price Book Entry | KQ_Id__c | KQ_Id__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | KQ_Pricebook2Id__c | KQ_Pricebook2Id | ssot__PriceBookEntry__dlm | Price Book Entry | KQ_PricebookId__c | KQ_PricebookId__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | LastModifiedById__c | Last Modified By ID | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__LastModifiedById__c | ssot__LastModifiedById__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | LastModifiedDate__c | Last Modified Date | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | Name__c | Product Name | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__Name__c | ssot__Name__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | Pricebook2Id__c | Price Book ID | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__PricebookId__c | ssot__PricebookId__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | Product2Id__c | Product ID | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__ProductId__c | ssot__ProductId__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | SystemModstamp__c | System Modstamp | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__SystemModstamp__c | ssot__SystemModstamp__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | UnitPrice__c | List Price | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__UnitListPriceAmount__c | ssot__UnitListPriceAmount__c |  |  |  |
| PricebookEntry_Home__dll | PricebookEntry_Home | UseStandardPrice__c | Use Standard Price | ssot__PriceBookEntry__dlm | Price Book Entry | ssot__UseStandardPrice__c | ssot__UseStandardPrice__c |  |  |  |

### ProductCategory_Home (`ProductCategory_Home__dll`) → Product Category (`ssot__ProductCategory__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ProductCategory_Home__dll | ProductCategory_Home | CatalogId__c | Catalog ID | ssot__ProductCategory__dlm | Product Category | ssot__ProductCatalogId__c | ssot__ProductCatalogId__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | CreatedDate__c | Created Date | ssot__ProductCategory__dlm | Product Category | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | DataSource__c | Data Source | ssot__ProductCategory__dlm | Product Category | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | DataSourceObject__c | Data Source Object | ssot__ProductCategory__dlm | Product Category | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | Description__c | Description | ssot__ProductCategory__dlm | Product Category | ssot__Description__c | ssot__Description__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | Id__c | Category ID | ssot__ProductCategory__dlm | Product Category | ssot__Id__c | ssot__Id__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | IsNavigational__c | Show In Menu | ssot__ProductCategory__dlm | Product Category | ssot__IsNavigational__c | ssot__IsNavigational__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | KQ_Id__c | KQ_Id | ssot__ProductCategory__dlm | Product Category | KQ_Id__c | KQ_Id__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | KQ_ParentCategoryId__c | KQ_ParentCategoryId | ssot__ProductCategory__dlm | Product Category | KQ_ParentCategoryId__c | KQ_ParentCategoryId__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | LastModifiedDate__c | Last Modified Date | ssot__ProductCategory__dlm | Product Category | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | Name__c | Name | ssot__ProductCategory__dlm | Product Category | ssot__Name__c | ssot__Name__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | ParentCategoryId__c | Category ID | ssot__ProductCategory__dlm | Product Category | ssot__ParentCategory__c | ssot__ParentCategory__c |  |  |  |
| ProductCategory_Home__dll | ProductCategory_Home | ParentCategoryId__c | Category ID | ssot__ProductCategory__dlm | Product Category | ssot__ParentCategoryId__c | ssot__ParentCategoryId__c |  |  |  |

### Promotion_Home (`Promotion_Home__dll`) → Promotion (`ssot__Promotion__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Promotion_Home__dll | Promotion_Home | CampaignId__c | Campaign ID | ssot__Promotion__dlm | Promotion | ssot__PrimaryCampaignId__c | ssot__PrimaryCampaignId__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | CreatedById__c | Created By ID | ssot__Promotion__dlm | Promotion | CreatedById__c | CreatedById__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | CreatedDate__c | Created Date | ssot__Promotion__dlm | Promotion | ssot__CreatedDate__c | ssot__CreatedDate__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | DataSource__c | Data Source | ssot__Promotion__dlm | Promotion | ssot__DataSourceId__c | ssot__DataSourceId__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | DataSourceObject__c | Data Source Object | ssot__Promotion__dlm | Promotion | ssot__DataSourceObjectId__c | ssot__DataSourceObjectId__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | Description__c | Description | ssot__Promotion__dlm | Promotion | ssot__Description__c | ssot__Description__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | DisplayName__c | Display Name | ssot__Promotion__dlm | Promotion | ssot__DisplayName__c | ssot__DisplayName__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | Id__c | Promotion ID | ssot__Promotion__dlm | Promotion | ssot__Id__c | ssot__Id__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | IsActive__c | Active | ssot__Promotion__dlm | Promotion | ssot__IsActive__c | ssot__IsActive__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | IsAutomatic__c | Automatic | ssot__Promotion__dlm | Promotion | ssot__IsAutomatic__c | ssot__IsAutomatic__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | IsCommercePromotion__c | Commerce Promotion | ssot__Promotion__dlm | Promotion | ssot__IsCommercePromotion__c | ssot__IsCommercePromotion__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | KQ_CampaignId__c | KQ_CampaignId | ssot__Promotion__dlm | Promotion | KQ_PrimaryCampaignId__c | KQ_PrimaryCampaignId__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | KQ_Id__c | KQ_Id | ssot__Promotion__dlm | Promotion | KQ_Id__c | KQ_Id__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | LastModifiedDate__c | Last Modified Date | ssot__Promotion__dlm | Promotion | ssot__LastModifiedDate__c | ssot__LastModifiedDate__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | Name__c | Name | ssot__Promotion__dlm | Promotion | ssot__Name__c | ssot__Name__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | Objective__c | Objective | ssot__Promotion__dlm | Promotion | ssot__ObjectiveText__c | ssot__ObjectiveText__c |  |  |  |
| Promotion_Home__dll | Promotion_Home | QualifierCriteria__c | Qualifier Criteria | ssot__Promotion__dlm | Promotion | ssot__DiscountExclusivityTypeId__c | ssot__DiscountExclusivityTypeId__c |  |  |  |

### StaticCurrencyRates_Home__dll (`StaticCurrencyRates_Home__dll`) → Static Currency Rates Home (`StaticCurrencyRates_Home__dlm`)

| Source DLO API Name | Source DLO Label | Source Field API Name | Source Field Label | Target DMO API Name | Target DMO Label | Target DMO Attribute API Name | Target Attribute Label | Data Source Field | Business Label | Manual Mapping |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| StaticCurrencyRates_Home__dll | StaticCurrencyRates_Home__dll | DataSource__c | DataSource__c | StaticCurrencyRates_Home__dlm | Static Currency Rates Home | DataSourceId__c | DataSourceId__c |  |  |  |
| StaticCurrencyRates_Home__dll | StaticCurrencyRates_Home__dll | DataSourceObject__c | DataSourceObject__c | StaticCurrencyRates_Home__dlm | Static Currency Rates Home | DataSourceObjectId__c | DataSourceObjectId__c |  |  |  |
| StaticCurrencyRates_Home__dll | StaticCurrencyRates_Home__dll | FromISOCurrencyCode__c | FromISOCurrencyCode__c | StaticCurrencyRates_Home__dlm | Static Currency Rates Home | FromISOCurrencyCode__c | FromISOCurrencyCode__c |  |  |  |
| StaticCurrencyRates_Home__dll | StaticCurrencyRates_Home__dll | Id__c | Id__c | StaticCurrencyRates_Home__dlm | Static Currency Rates Home | Id__c | Id__c |  |  |  |
| StaticCurrencyRates_Home__dll | StaticCurrencyRates_Home__dll | InternalOrganization__c | InternalOrganization__c | StaticCurrencyRates_Home__dlm | Static Currency Rates Home | InternalOrganizationId__c | InternalOrganizationId__c |  |  |  |
| StaticCurrencyRates_Home__dll | StaticCurrencyRates_Home__dll | KQ_Id__c | KQ_Id__c | StaticCurrencyRates_Home__dlm | Static Currency Rates Home | KQ_Id__c | KQ_Id__c |  |  |  |
| StaticCurrencyRates_Home__dll | StaticCurrencyRates_Home__dll | RateDenominatorNumber__c | RateDenominatorNumber__c | StaticCurrencyRates_Home__dlm | Static Currency Rates Home | RateDenominatorNumber__c | RateDenominatorNumber__c |  |  |  |
| StaticCurrencyRates_Home__dll | StaticCurrencyRates_Home__dll | RateNumeratorNumber__c | RateNumeratorNumber__c | StaticCurrencyRates_Home__dlm | Static Currency Rates Home | RateNumeratorNumber__c | RateNumeratorNumber__c |  |  |  |
| StaticCurrencyRates_Home__dll | StaticCurrencyRates_Home__dll | ToISOCurrencyCode__c | ToISOCurrencyCode__c | StaticCurrencyRates_Home__dlm | Static Currency Rates Home | ToISOCurrencyCode__c | ToISOCurrencyCode__c |  |  |  |

## Relationships

DMO-to-DMO relationships, read from `sourceObject`/`targetObject` in the relationships payload. **Object** is the source entity; **Related Object** is what it links to. **Status** is shown so inactive standard relationships are visible (not dropped). Blank cells mean the payload did not expose that property.

| Object | Field | Cardinality | Related Object | Related Field | Status |
| --- | --- | --- | --- | --- | --- |
| Experiment Log | ssot__Individualid__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Academic Credential | ssot__IssuerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Academic Session Attendance | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Academic Term Enrollment | ssot__LearnerAccountId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Academic Term Enrollment | ssot__LearnerContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__AutoPaymentMethodId__c | N:1 | ssot__PaymentMethod__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__AutoPaymentMethodId__c | N:1 | ssot__Voucher__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__BillContactAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | ACTIVE |
| Account | ssot__FaxPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | ACTIVE |
| Account | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__OperatingHoursId__c | N:1 | ssot__OperatingHours__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__OrderDeliveryMethodId__c | N:1 | ssot__OrderDeliveryMethod__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__OwnerId__c | N:1 | ssot__User__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__ParentAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | ACTIVE |
| Account | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__PrimarySalesContactPointId__c | N:1 | ssot__ContactPoint__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__PrimarySalesContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__PrimarySalesContactPointId__c | N:1 | ssot__ContactPointApp__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__PrimarySalesContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__PrimarySalesContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__PrimarySalesContactPointId__c | N:1 | ssot__ContactPointSocial__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__PrimarySalesRepId__c | N:1 | ssot__User__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__SalesPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | ACTIVE |
| Account | ssot__ShippingAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__ShippingContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__ShippingEmailId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Account | ssot__ShippingPhoneid__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | ACTIVE |
| Account Contact | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Account Contact | ssot__BusinessPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | ACTIVE |
| Account Contact | ssot__ContactEmailId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | ACTIVE |
| Account Contact | ssot__FaxPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | ACTIVE |
| Account Contact | ssot__HomePhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | ACTIVE |
| Account Contact | ssot__IndirectRelationAccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Account Contact | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | ACTIVE |
| Account Contact | ssot__MailingAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | ACTIVE |
| Account Contact | ssot__MobilePhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | ACTIVE |
| Account Contact | ssot__OtherContactAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Account Contact | ssot__OwnerId__c | N:1 | ssot__User__dlm | ssot__Id__c | INACTIVE |
| Account Contact | ssot__ReportsToAccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | ACTIVE |
| Actionable List Member | ssot__ReferenceRecordId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Actionable List Member | ssot__ReferenceRecordId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Action Plan | ssot__TargetId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Action Plan | ssot__TargetId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Action Plan Item | ssot__TargetId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Action Plan Item | ssot__TargetId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Action Plan Template | ssot__TargetEntityTypeId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Action Plan Template | ssot__TargetEntityTypeId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Activity Participant | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Activity Participant | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Activity Participant | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Activity Participant | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Activity Topic | ssot__RelatedToId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Address | ssot__ContactPointPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Adverse Event | ssot__RecordedById__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Adverse Event | ssot__SubjectId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Adverse Event Cause | ssot__AuthoredById__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Adverse Event Cause | ssot__AuthoredById__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Adverse Event Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Adverse Event Party | ssot__PartyId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Adverse Event Party | ssot__PartyId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Affiliation | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| AI Agent Interaction | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| AI Agent Interaction Message | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| AI Agent Session | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| AI Agent Session Participant | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Air Travel Energy Use | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Allergy Intolerance | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Allergy Intolerance | ssot__AssertionSourceId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Allergy Intolerance | ssot__RecorderId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Annual Emissions Inventory | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Anti-Corruption Initiative Summary | ssot__SubsidiaryAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Application | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Application | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Application | ssot__Approver__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Application | ssot__SubmittedBy__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Application | ssot__SubmittedBy__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Application Decision | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Application Recommender | ssot__RecommenderId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Application Review | ssot__InstitutionId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Assessment | ssot__SubjectId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Assessment | ssot__SubjectId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Assessment Envelope | ssot__RecipientId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Assessment Envelope | ssot__RecipientId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Assessment Signature | ssot__SigneeId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Assessment Signature | ssot__SigneeObjectName__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Asset | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Asset | ssot__BillToAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Asset | ssot__PrimaryContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Asset | ssot__ServicePartnerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Asset | ssot__ServicerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Asset | ssot__SupplierAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Asset Participant | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Asset Participant | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Asset Warranty Term | ssot__PriceBookId__c | N:1 | ssot__PriceBook__dlm | ssot__Id__c | INACTIVE |
| Authorization Form Consent | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Authorization Form Consent | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Benefit Assignment | ssot__EnrolleeId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Benefit Assignment | ssot__EnrolleeId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Benefit Assignment | ssot__ProviderId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Benefit Disbursement | ssot__RecipientId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Benefit Disbursement | ssot__RecipientId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Benefit Provider Searchable Field | ssot__OperatingHoursId__c | N:1 | ssot__OperatingHours__dlm | ssot__Id__c | INACTIVE |
| Budget | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Bulk Email Message | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | ACTIVE |
| Bulk Email Message | ssot__CommunicationSubscriptionChannelTypeId__c | N:1 | ssot__CommunicationSubscriptionChannelType__dlm | ssot__Id__c | INACTIVE |
| Bulk Email Message | ssot__DigitalContentId__c | N:1 | ssot__DigitalContent__dlm | ssot__Id__c | INACTIVE |
| Bulk Email Message | ssot__EmailContentId__c | N:1 | ssot__EmailContent__dlm | ssot__Id__c | INACTIVE |
| Bulk Email Message | ssot__FlowElementId__c | N:1 | ssot__FlowElement__dlm | ssot__Id__c | INACTIVE |
| Bulk Email Message | ssot__MarketAudienceId__c | N:1 | ssot__MarketAudience__dlm | ssot__Id__c | INACTIVE |
| Bulk Email Message | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Bulk Message | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Bulk Message | ssot__DigitalContentId__c | N:1 | ssot__DigitalContent__dlm | ssot__Id__c | INACTIVE |
| Bulk Message | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Bundle Product | ssot__PrimaryProductCategory__c | N:1 | ssot__ProductCategory__dlm | ssot__Id__c | INACTIVE |
| Business Milestone | ssot__PrimaryAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Buyer Intent | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Buyer Intent | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Campaign | ssot__ParentCampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | ACTIVE |
| Campaign Member | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Campaign Member | ssot__ContactPointPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Campaign Member | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Campaign Member | ssot__IndividualSourceId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Care Barrier | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Determinant | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Metric Target | ssot__Patient__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Observation | ssot__ObservedSubjectAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Observation | ssot__ObserverId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Observation Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Plan | ssot__AuthorId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Plan | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Plan | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Care Plan Activity Detail | ssot__DetailRecordId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Plan Detail | ssot__DetailRecordId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Plan Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Preauthorization | ssot__PayerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Program | ssot__SponsorId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Program Campaign | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Care Program Enrollee | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Program Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Program Provider Product | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Program Site | ssot__SponsorRepresentativeId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Care Program Team Member | ssot__MemberId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Request | ssot__GeneralPractitionerId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Care Request | ssot__MemberAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Request | ssot__RequestingPractitionerId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Care Request | ssot__ServicingPractitionerId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Care Request Diagnosis Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Request Drug | ssot__DispensingPharmacyId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Care Request Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Case | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Case | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Case | ssot__CaseSupportWorkHoursId__c | N:1 | ssot__OperatingHours__dlm | ssot__Id__c | INACTIVE |
| Case | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Case Episode | ssot__EpisodeAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Case Episode | ssot__SubjectId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Case Episode | ssot__SubjectId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Case Milestone | ssot__OperatingHoursId__c | N:1 | ssot__OperatingHours__dlm | ssot__Id__c | INACTIVE |
| Case Participant | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Case Participant | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Case Proceeding Participant | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Case Proceeding Participant | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Category | ssot__ParentCategoryId__c | N:1 | ssot__Category__dlm | ssot__Id__c | INACTIVE |
| Channel Engagement | ssot__BulkEmailMessageId__c | N:1 | ssot__BulkEmailMessage__dlm | ssot__Id__c | INACTIVE |
| Channel Engagement | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Channel Engagement | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Claim | ssot__ClaimantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Claim | ssot__ClaimantId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Claim | ssot__InsurerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Claim | ssot__ResponsiblePartyId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Claim Participant | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Claim Participant | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Claim Participant | ssot__ParticipantId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Clinical Encounter | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Clinical Encounter | ssot__DestinationOrganizationId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Clinical Encounter | ssot__PreviousOrganizationId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Clinical Encounter Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Clinical Service Request | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Clinical Service Request | ssot__PerformerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Clinical Service Request | ssot__RequesterId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Clinical Service Request Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Collection Plan | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Communication Subscription Channel Type | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Communication Subscription Consent | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Complaint | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Complaint | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Complaint Participant | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Complaint Participant | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Compliance Policy | ssot__PolicyRepresentativeId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Constituent Role | ssot__InstitutionId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Constituent Role | ssot__PersonId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Consumed Location Product | ssot__PriceBookEntryId__c | N:1 | ssot__PriceBookEntry__dlm | ssot__Id__c | INACTIVE |
| Contact Point Address | ssot__AddressId__c | N:1 | ssot__Address__dlm | ssot__Id__c | INACTIVE |
| Contact Point Address | ssot__ContactPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Contact Point Address | ssot__PartyId__c | N:1 | ssot__Account__dlm | ssot__Id__c | ACTIVE |
| Contact Point Address | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Contact Point Address | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | ACTIVE |
| Contact Point Address | ssot__PhysicalLocationId__c | N:1 | ssot__Location__dlm | ssot__Id__c | INACTIVE |
| Contact Point Address | ssot__StateProvinceId__c | N:1 | ssot__StateProvince__dlm | ssot__Id__c | INACTIVE |
| Contact Point App | ssot__PartyId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Contact Point App | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Contact Point Consent | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Contact Point Consent | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Contact Point Consent | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Contact Point Consent | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Contact Point Digital Id | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Contact Point Email | ssot__PartyId__c | N:1 | ssot__Account__dlm | ssot__Id__c | ACTIVE |
| Contact Point Email | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | ACTIVE |
| Contact Point OTT Service | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Contact Point Phone | ssot__DeviceId__c | N:1 | ssot__Device__dlm | ssot__Id__c | INACTIVE |
| Contact Point Phone | ssot__PartyId__c | N:1 | ssot__Account__dlm | ssot__Id__c | ACTIVE |
| Contact Point Phone | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | ACTIVE |
| Contact Point Social | ssot__PartyId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Contact Point Social | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Contract | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Contract | ssot__BillToAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Contract | ssot__CustomerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Contract | ssot__PriceBookId__c | N:1 | ssot__PriceBook__dlm | ssot__Id__c | INACTIVE |
| Contract | ssot__ShipToAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Contract Line | ssot__PriceBookEntryId__c | N:1 | ssot__PriceBookEntry__dlm | ssot__Id__c | INACTIVE |
| Conv Channel Engagement Summary | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Conv Channel Engagement Summary | ssot__PartnerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Conv Channel Engagement Summary | ssot__RelatedRecordId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Conv Chnl Engmt Summary Participant | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Coupon | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Course Offering | ssot__PrimaryFacultyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Course Offering Participant | ssot__ParticipantAccountId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Course Offering Participant | ssot__ParticipantContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Course Offering Participant Result | ssot__EvaluatorContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Coverage Benefit | ssot__MemberId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Coverage Benefit Item | ssot__MemberId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Coverage Benefit Verification Request | ssot__EnteredById__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Coverage Benefit Verification Request | ssot__PayerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Credit Tender | ssot__CreditAssignmentAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Custody Chain Entry | ssot__CustodianId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Custody Chain Entry | ssot__CustodianId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Device Application Engagement | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Device Application Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Device Application Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Device Application Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Device Application Engagement | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Device Application Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Device Application Engagement | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Diagnostic Summary | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Diagnostic Summary | ssot__AuthenticatorId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Diagnostic Summary | ssot__AuthenticatorId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Diagnostic Summary | ssot__CustodianOrganizationId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Diagnostic Summary Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Digital Content | ssot__TemplateId__c | N:1 | ssot__DigitalContent__dlm | ssot__Id__c | INACTIVE |
| Disclosure Reporting Period | ssot__AffiliateAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Diversity Equity Inclusion Summary | ssot__SubsidiaryAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Document Checklist Item | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Document Checklist Item | ssot__FileOwnerId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Document Checklist Item | ssot__ParentRecordId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Donor Gift Summary | ssot__DonorId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Donor Gift Summary | ssot__FirstGiftCampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Driver Performance Summary | ssot__ContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Economic Performance Summary | ssot__SubsidiaryAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Educational Info Request | ssot__RequesterId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Education Application | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Education Application | ssot__SubmittedByContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Email Engagement | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Email Engagement | ssot__BulkEmailMessageId__c | N:1 | ssot__BulkEmailMessage__dlm | ssot__Id__c | INACTIVE |
| Email Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Email Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Email Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Email Engagement | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Email Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Email Engagement | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Email Engagement Frequency | ssot__ContactPointEmailId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Email Engagement Score | ssot__ContactPointEmailId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Email Message | ssot__RelatedToId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Email Publication | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Email Send Time Optimization | ssot__ContactPointEmailId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Employee | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Employee Demographic Summary | ssot__SubsidiaryAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Employee Development Summary | ssot__SubsidiaryAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Employment Benefit Summary | ssot__SubsidiaryAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Engagement Action | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Engagement Action | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Engagement Analysis Text Participant | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Engagement Analysis Text Participant | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Engagement Analysis Text Participant | ssot__ParticipantId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Engagement Channel Participant | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Engagement Channel Participant | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Engagement Channel Participant | ssot__ParticipantId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Engagement Channel Type Consent | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Engagement Participant App Role | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Engagement Participant App Role | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Engagement Participant App Role | ssot__ParticipantId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Engagement Topic | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Engagement Topic | ssot__RelatedToId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Financial Account Party | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Financial Account Party | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Financial Customer | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | ACTIVE |
| Financial Holding | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Financial Plan | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Flow | ssot__AssociatedRecordId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Flow Run | ssot__PrimaryRecordId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Fulfillment Order | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Fulfillment Order | ssot__ContactPointAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Fulfillment Order | ssot__FulfilledToPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Fulfillment Order Price Adjustment | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Fulfillment Order Product Price Adj | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Funding Award | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Funding Award | ssot__AwardeeId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Funding Award Requirement | ssot__AssignedContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Game Participant | ssot__ParticipantId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Game Participant | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Gift Commitment Change Attribution Log | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Gift Commitment | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Gift Commitment | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Gift Commitment | ssot__DonorId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Gift Commitment Schedule | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Gift Default Designation | ssot__ParentRecordId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Gift Entry | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Gift Entry | ssot__DonorId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Gift Soft Credit | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Gift Soft Credit | ssot__RecipientId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| GiftTransaction | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| GiftTransaction | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| GiftTransaction | ssot__DonorId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Goal Assignment | ssot__AssignedByRecordId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Goal Assignment | ssot__AssignedByRecordId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Goal Assignment | ssot__GoalAssigneeId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Goal Assignment | ssot__GoalAssigneeId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Goal Assignment | ssot__ParentRecordId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Goods Product | ssot__PrimaryProductCategory__c | N:1 | ssot__ProductCategory__dlm | ssot__Id__c | INACTIVE |
| Government Financial Assistance Summary | ssot__SubsidiaryAccountd__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Ground Travel Energy Use | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Healthcare Facility | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Healthcare Facility Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Healthcare Performer | ssot__PerformerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Healthcare Practitioner Facility | ssot__PractitionerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Healthcare Practitioner Facility | ssot__PractitionerId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Healthcare Provider | ssot__ProviderServiceOrgAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Health Score | ssot__SubjectId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Health Score | ssot__SubjectId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Hlthcr Practitioner Facility Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Hotel Stay Energy Use | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Household | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Identity Match | ssot__MatchingRecordId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Identity Match | ssot__RecordId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Incident | ssot__OperatingHoursId__c | N:1 | ssot__OperatingHours__dlm | ssot__Id__c | INACTIVE |
| Individual | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | ACTIVE |
| Individual | ssot__PrimaryAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | ACTIVE |
| Inventory Product Disbursement | ssot__DisbursementTargetAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Inventory Request | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Inventory Request Item | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Job Application Searchable Field | ssot__ApplicantAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Knowledge Article Category | ssot__CategoryId__c | N:1 | ssot__Category__dlm | ssot__Id__c | INACTIVE |
| Knowledge Article Engagement | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Knowledge Article Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Lead | ssot__ContactAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Lead | ssot__ContactPointEmailId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Lead | ssot__ConvertedToAccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Lead | ssot__ConvertedToAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Lead | ssot__FaxContactPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Lead | ssot__MobileContactPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Lead | ssot__PartnerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Lead | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Lead | ssot__PhoneContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Lead Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Lead Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Learner Campus Spaces Activity | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Learner Learning System Activity | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Learner Learning System Activity | ssot__LearningManagementSystemId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Learner Learning System Activity | ssot__LMSId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Learner Pathway | ssot__LearnerContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Learner Profile | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Learner Program | ssot__LearnerAccountId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Learner Program | ssot__LearnerContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Learning | ssot__ProviderId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Learning Achievement | ssot__IssuerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Learning Course | ssot__ProviderId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Learning Program | ssot__ProviderId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Learning Program Plan | ssot__ProviderId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Life Science Drug Distribution Data | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Life Science Drug Prescription Data | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Location | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Location | ssot__OperatingHoursId__c | N:1 | ssot__OperatingHours__dlm | ssot__Id__c | INACTIVE |
| Loyalty Ledger | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Loyalty Pgm Engmt Attribute Promotion | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Loyalty Pgm Group Member Relationship | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Loyalty Pgm Group Member Relationship | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Loyalty Program Member | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Loyalty Program Member | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Loyalty Program Member | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Loyalty Program Member | ssot__ReferredByPartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Loyalty Program Member Promotion | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Loyalty Program Partner | ssot__PartnerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Loyalty Program Partner | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Loyalty Program Partner Ledger | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Loyalty Program Partner Promotion | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Loyalty Transaction Journal | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Loyalty Transaction Journal | ssot__ProductCategoryId__c | N:1 | ssot__ProductCategory__dlm | ssot__Id__c | INACTIVE |
| Marketing Journey Activity Run | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Master Product | ssot__PrimaryProductCategory__c | N:1 | ssot__ProductCategory__dlm | ssot__Id__c | INACTIVE |
| Meal Card Activity | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Media Engagement | ssot__DigitalContentId__c | N:1 | ssot__DigitalContent__dlm | ssot__Id__c | INACTIVE |
| Media Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Media Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Medication | ssot__ManufacturerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Medication Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Member Plan | ssot__MemberAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Member Plan | ssot__MemberIndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Member Plan | ssot__PayerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Member Plan | ssot__SubscriberIndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Mentoring Profile | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Message Engagement | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Message Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Message Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Message Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Message Engagement | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Message Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Message Engagement | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Network Usage | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Offer | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Offer | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Offer Market Segment | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Offer Product Category | ssot__ProductCategoryId__c | N:1 | ssot__ProductCategory__dlm | ssot__Id__c | INACTIVE |
| Operating Hours Time Slot | ssot__OperatingHoursId__c | N:1 | ssot__OperatingHours__dlm | ssot__Id__c | INACTIVE |
| Opportunity | ssot__CustomerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Opportunity | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Opportunity | ssot__PartnerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Opportunity Contact | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | ACTIVE |
| Opportunity Contact | ssot__OpportunityId__c | N:1 | ssot__Opportunity__dlm | ssot__Id__c | INACTIVE |
| Opportunity Influence | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Opportunity Influence | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Order Delivery Method | ssot__OrderDeliverySupplierAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Organization Incident Summary | ssot__SubsidiaryAccount__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Outreach Source Code | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Outreach Summary | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Party | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | ACTIVE |
| Party Accreditation | ssot__IssuingPartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Accreditation | ssot__ReceivingPartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Award | ssot__IssuingPartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Award | ssot__ReceivingPartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Board Certification | ssot__IssuingPartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Board Certification | ssot__ReceivingPartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Board Certification Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Business License | ssot__ContactPointAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Party Business License | ssot__IssuingPartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Business License | ssot__ReceivingPartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Expense | ssot__PayeeId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Expense | ssot__PayerId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Financial Asset | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Financial Liability | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Identification | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Party Income | ssot__EmployerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Income | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Interest Tag | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Assessment | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Assessment | ssot__AssessmentOrganizationId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Assessment | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Indicator | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Indicator | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Indicator | ssot__ParticipantId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Indicator | ssot__RelatedOrganizationId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Milestone | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Milestone | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Occurrence | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Occurrence | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Occurrence | ssot__ParticipantId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Party Philanthropic Occurrence | ssot__RelatedOrganizationId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Profile | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Party Profile | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Profile | ssot__HouseholdAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Party Profile | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Publication | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Related Party | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Party Related Party | ssot__RelatedPartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Patient Health Condition | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Health Condition | ssot__AssertionSourceId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Health Condition | ssot__RecordCreatorReferenceId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Immunization | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Immunization | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Patient Immunization Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medical Procedure | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medical Procedure | ssot__AssertionSourceId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| PatientMedicalProcedureIdentifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Dispense | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Dispense | ssot__CollectedById__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Dispense | ssot__CollectedById__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Dosage | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Reconciliation | ssot__PatientId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Request | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Request | ssot__DispenserId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Request | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Request | ssot__PerformerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Request | ssot__RequesterId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Request | ssot__SecondaryInformationSourceId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Statement | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Statement | ssot__StatementSourceId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Medication Statement Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Registered Device | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Patient Registered Device Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Payment Instrument | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Payment Method | ssot__AccountID__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Payment Request | ssot__FacilityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Payment Request | ssot__RemittanceRecipientId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Payment Request | ssot__ServiceProviderId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Payment Request | ssot__ServiceProviderId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Payment Request | ssot__ServiceRecipientId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Payment Request | ssot__ServiceRecipientId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Payment Request | ssot__SubmittingAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Payment Request Line | ssot__FacilityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Payment Request Line | ssot__ServiceProviderId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Payment Request Line | ssot__ServiceProviderId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Person Academic Credential | ssot__LearnerContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Personalization Decision | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Personalization Log | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Person Disability | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Person Education | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Person Education | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Person Education | ssot__InstitutionAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Person Employment | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Person Employment | ssot__EmployerContactPointAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Person Employment | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Person Examination | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Person Examination | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Person Language | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Person Life Event | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Person Name | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Person Public Profile | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Person Public Profile Preference Set | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Person Skill | ssot__PersonId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Person Skill | ssot__PersonId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Presentation Click Stream Entry | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Presentation Party Access | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Price Adjustment Group | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Price Book Entry | ssot__CreatedById__c | N:1 | ssot__User__dlm | ssot__Id__c | INACTIVE |
| Price Book Entry | ssot__LastModifiedById__c | N:1 | ssot__User__dlm | ssot__Id__c | INACTIVE |
| Price Book Entry | ssot__PricebookId__c | N:1 | ssot__PriceBook__dlm | ssot__Id__c | ACTIVE |
| Price Book Entry | ssot__ProductId__c | N:1 | ssot__Product__dlm | ssot__Id__c | INACTIVE |
| Privacy Consent Log | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Privacy Consent Log | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Privacy Consent Log | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Privacy Consent Log | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Privacy Consent Log | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Product | ssot__ServiceProviderAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Product Browse Engagement | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Product Browse Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Product Browse Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Product Browse Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Product Browse Engagement | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Product Browse Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Product Browse Engagement | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Product Category | ssot__ParentCategoryId__c | N:1 | ssot__ProductCategory__dlm | ssot__Id__c | ACTIVE |
| Product Category | ssot__ProductCatalogId__c | N:1 | ssot__ProductCatalog__dlm | ssot__Id__c | INACTIVE |
| Product Category Product | ssot__ProductCategoryId__c | N:1 | ssot__ProductCategory__dlm | ssot__Id__c | INACTIVE |
| Product Order Engagement | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Product Order Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Product Order Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Product Order Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Product Order Engagement | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Product Order Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Product Order Engagement | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Product Order Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Program Enrollment | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Program Enrollment | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Promotion | ssot__DefaultVoucherDefinitionId__c | N:1 | ssot__VoucherDefinition__dlm | ssot__Id__c | INACTIVE |
| Promotion | ssot__LeadId__c | N:1 | ssot__Lead__dlm | ssot__Id__c | INACTIVE |
| Promotion | ssot__LoyaltyProgramCurrencyId__c | N:1 | ssot__LoyaltyProgramCurrency__dlm | ssot__Id__c | INACTIVE |
| Promotion | ssot__LoyaltyProgramId__c | N:1 | ssot__LoyaltyProgram__dlm | ssot__Id__c | INACTIVE |
| Promotion | ssot__PrimaryCampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | ACTIVE |
| Promotion Actionable List | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Promotion Channel | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Promotion Engagement | ssot__ContentSlotName__c | N:1 | ssot__DigitalContent__dlm | ssot__Id__c | INACTIVE |
| Promotion Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Promotion Engagement | ssot__PromotionObjectId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Promotion Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Promotion Item Engagement | ssot__ContentSlotName__c | N:1 | ssot__DigitalContent__dlm | ssot__Id__c | INACTIVE |
| Promotion Item Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Promotion Item Engagement | ssot__PromotionObjectId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Promotion Item Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Promotion Limit | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Promotion Loyalty Partner Product | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Promotion Market Segment | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Promotion Party Transaction | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Promotion Party Transaction | ssot__RelatedPartyId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Promotion Party Transaction | ssot__RelatedPartyId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Promotion Stage | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Prospect | ssot__ContactPointAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Prospect | ssot__ContactPointEmailId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Prospect | ssot__ContactPointPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Prospect | ssot__ConvertedAccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Prospect | ssot__ConvertedAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Prospect | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Provider Activity Goal | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Provider Offering | ssot__ContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Provider Visit | ssot__ShippingAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Purchaser Plan | ssot__PayerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Purchaser Plan Association | ssot__PurchaserId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Quote | ssot__CustomerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Quote Product | ssot__PriceBookEntryId__c | N:1 | ssot__PriceBookEntry__dlm | ssot__Id__c | INACTIVE |
| Record Alert | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Record Alert | ssot__ReferenceContextId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Referral | ssot__ClientId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Referral | ssot__ProductCategoryId__c | N:1 | ssot__ProductCategory__dlm | ssot__Id__c | INACTIVE |
| Referral | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Referral | ssot__ProviderId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Referral | ssot__ProviderId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Referral | ssot__ReferredPartyId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Referral | ssot__ReferredPartyId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Referral | ssot__ReferrerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Referral | ssot__ReferrerId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Regulation | ssot__RegulationManagerId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Regulatory Transaction Fee | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Rental Car Energy Use | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Research Study Candidate | ssot__CandidateId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Research Study Candidate Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Research Study Identifier | ssot__IssuingAuthorityId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Return Order | ssot__CustomerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Return Order Product Price Adjustment | ssot__Promotion__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Sales Order | ssot__BillToAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Sales Order | ssot__BillToAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Sales Order | ssot__BillToContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Sales Order | ssot__BilltoEmailId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Sales Order | ssot__BilltoPhoneNumberId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Sales Order | ssot__PricebookId__c | N:1 | ssot__PriceBook__dlm | ssot__Id__c | INACTIVE |
| Sales Order | ssot__ShipToAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Sales Order | ssot__ShipToContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Sales Order | ssot__ShipToEmailId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Sales Order | ssot__ShiptoPhoneNumberId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Sales Order Delivery Group | ssot__ContactPointAddressId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Sales Order Product | ssot__SellerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Sales Order Product Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Sales Territory Acct Prodt Message Score | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Sales Territory Acct Recommended Action | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Sales Territory Account Score | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Saved Application Reference | ssot__ApplicantId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Saved Application Reference | ssot__BusinessAccountNameId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Saved Application Reference | ssot__SubmittedByContactId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Scope 3 Emissions Source | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Service Appointment | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Service Appointment | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Service Appointment | ssot__ParentRecordId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Service Process Definition | ssot__AssociatedRecordId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Service Territory | ssot__OperatingHoursId__c | N:1 | ssot__OperatingHours__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart | ssot__BillToAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart | ssot__BillToContactPointPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart | ssot__PartyId__c | N:1 | ssot__Party__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart | ssot__ShipToAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart | ssot__ShipToContactPointPhoneId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart Engagement | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart Engagement | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart Engagement | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart Product Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Shopping Cart Product Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Shopping Wishlist Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Shopping Wishlist Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Shopping Wishlist Item Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Shopping Wishlist Item Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| SMS Publication | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Social Contribution Summary | ssot__SubsidiaryAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Social Message Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Social Message Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Specimen | ssot__CollectorRecordId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Specimen | ssot__SourceReferenceRecordId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Stationary Asset Energy Use | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Success Team | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Success Team | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Suggested Assessment Definition | ssot__SubjectId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Survey Invitation | ssot__ParticipantId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Survey Response | ssot__SubmitterId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Survey Subject | ssot__SurveySubjectId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Tax Disclosure Summary | ssot__SubsidiaryAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Team Member | ssot__MemberId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Telematics Provider | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| User | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| User | ssot__ContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Vehicle | ssot__CurrentOwnerId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Vehicle Asset Energy Use | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Vetting Evaluation | ssot__SubjectId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Video Call | ssot__RelatedToId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Video Call | ssot__RelatedToId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Visit | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Voice Call | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Voice Call | ssot__RelatedToId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Voice Call | ssot__RelatedToId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Voucher | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Voucher | ssot__AccountID__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Voucher | ssot__PartyId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Voucher | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Voucher Definition | ssot__PartnerAccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Warranty Term | ssot__PriceBookId__c | N:1 | ssot__PriceBook__dlm | ssot__Id__c | INACTIVE |
| Web Search Engagement | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Web Search Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Web Search Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Web Search Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Web Search Engagement | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Web Search Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Web Search Engagement | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Web Search Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Website Engagement | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Website Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointAddress__dlm | ssot__Id__c | INACTIVE |
| Website Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointEmail__dlm | ssot__Id__c | INACTIVE |
| Website Engagement | ssot__ContactPointId__c | N:1 | ssot__ContactPointPhone__dlm | ssot__Id__c | INACTIVE |
| Website Engagement | ssot__EngagementChannelTypeId__c | N:1 | ssot__EngagementChannelType__dlm | ssot__Id__c | INACTIVE |
| Website Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Website Engagement | ssot__MarketSegmentId__c | N:1 | ssot__MarketSegment__dlm | ssot__Id__c | INACTIVE |
| Website Engagement | ssot__PromotionId__c | N:1 | ssot__Promotion__dlm | ssot__Id__c | INACTIVE |
| Website Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Website Item Engagement | ssot__IndividualId__c | N:1 | ssot__Individual__dlm | ssot__Id__c | INACTIVE |
| Website Item Engagement | ssot__UtmId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Website Publication | ssot__CampaignId__c | N:1 | ssot__Campaign__dlm | ssot__Id__c | INACTIVE |
| Website Publication | ssot__DigitalContentId__c | N:1 | ssot__DigitalContent__dlm | ssot__Id__c | INACTIVE |
| Work Order | ssot__AccountContactId__c | N:1 | ssot__AccountContact__dlm | ssot__Id__c | INACTIVE |
| Work Order | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Work Order | ssot__OperatingHoursId__c | N:1 | ssot__OperatingHours__dlm | ssot__Id__c | INACTIVE |
| Work Order | ssot__PriceBookId__c | N:1 | ssot__PriceBook__dlm | ssot__Id__c | INACTIVE |
| Work Order Item | ssot__PriceBookEntryId__c | N:1 | ssot__PriceBookEntry__dlm | ssot__Id__c | INACTIVE |
| Work Resource | ssot__AccountId__c | N:1 | ssot__Account__dlm | ssot__Id__c | INACTIVE |
| Work Type | ssot__OperatingHoursId__c | N:1 | ssot__OperatingHours__dlm | ssot__Id__c | INACTIVE |

## Identity Resolution Rules

_No Identity Resolution Rules found._

## Calculated Insights

_No Calculated Insights found._
