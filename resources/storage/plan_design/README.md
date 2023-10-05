**5.1 Planning and Design**
---------------------------

<table>
    <thead>
        <tr class="header">
            <th><strong>Requirement</strong></th>
            <th><strong>Procedure</strong> [Role - Data Steward (DS) or Data Engineer (DE)]</th>
        </tr>
    </thead>
    <tbody>
        <tr class="odd">
            <td>A5.1.1 Define storage metrics to be collected</td>
            <td>B5.1.1 Implement bucket inventories and associated detailed metrics [DE]</td>
        </tr>
        <tr class="even">
            <td>A5.1.2 Develop storage and egress cost estimates</td>
            <td>
                <p>B5.1.2 Use data sheet (B1.1.4) to generate storage and egress <a
                        href="https://www.cloudysave.com/aws/cost-calculator/"><span class="underline">costs using this
                            calculator</span></a>. Costs to consider include total product size, whether redundant
                    storage for operations and backup/archive are require], projected growth, and estimated use[DE]</p>
                <ul>
                    <li>
                        <blockquote>
                            <p><a
                                    href="https://drive.google.com/file/d/1mLtWKImjQQixeZOWl0SVx7BkA_KXxBox/view?usp=share_link"><span
                                        class="underline">ESDIS template</span></a></p>
                        </blockquote>
                    </li>
                </ul>
            </td>
        </tr>
        <tr class="odd">
            <td>A5.1.3 Define the S3 Bucket structure including the naming convention, tagging, logs, etc.</td>
            <td>B5.1.3 Adopt <a
                    href="https://docs.google.com/document/d/16oStNf6eRKFUjH5D11a4Vwxsn24a4TVr8HRLIqruHTU/edit"><span
                        class="underline">these best practices</span></a> for key aspects of cloud storage [DS + DE]
            </td>
        </tr>
        <tr class="even">
            <td>A5.1.4 Define data storage environments needed such as sandbox, development, staging, production
                (operational + backup copies)</td>
            <td>B5.1.4 Recommend creating a minimum of three storage environments - sandbox, development/staging and
                production. [DE]</td>
        </tr>
        <tr class="odd">
            <td>A5.1.5 Define storage policy for retention including the rules for defining which storage class to use
                and when the storage class should be changed</td>
            <td>
                <p>B5.1.5 For a rolling archive with capped storage capacity, use information in the <a
                        href="https://docs.google.com/document/d/16oStNf6eRKFUjH5D11a4Vwxsn24a4TVr8HRLIqruHTU/edit"><span
                            class="underline">best practices document</span></a>. [DE]</p>
                <ul>
                    <li>
                        <blockquote>
                            <p>If selected metrics show that the usage for a dataset is below a threshold, then the
                                dataset should be moved to cold storage or deleted</p>
                        </blockquote>
                    </li>
                    <li>
                        <blockquote>
                            <p>Storage class can be changed manually (s3 cli) or by setting bucket specific rules. These
                                rules or changes should be cost based (or time based) - need to determine at what usage
                                it becomes more costly to store and retrieve from “colder” storage class versus keeping
                                data in “warmer class” (i.e. &lt;~40% of total dataset egress it becomes cheaper to use
                                IA vs standard storage)</p>
                        </blockquote>
                    </li>
                </ul>
            </td>
        </tr>
        <tr class="even">
            <td>A5.1.6 Define storage policy for retiring data</td>
            <td>B5.1.6 The retired dataset should be moved to cold storage or deleted [<a
                    href="https://docs.google.com/document/d/1cmqX_CMLQyCtpB3nMyEOyKear4BmYPvtK6SZfjqhM74/edit?pli=1"><span
                        class="underline">draft CSDA retirement document</span></a> [DE]</td>
        </tr>
    </tbody>
</table>
