# Ledger Self-Consistency Vote

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ledger-self-consistency-vote-2cec5deb3656`
Run ID: `ledger-self-consistency-vote-2cec5deb3656-20260605T043744064537+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/96acb1bd8a94

## What looked useful

Weak internal ledger self-consistency improved accuracy by +0.0625 to +0.2065 in independent/noisy conditions at K=3-5, but only +0.0008 to +0.0065 in larger-K coherent wrong-ledger conditions. Strict prompt-grounded ledger checking improved accuracy by +0.3944 at K=5 for systematic omission and +0.5126 at K=5 for systematic wrong ledgers.

## Boundaries and scale limits

No real LLM generations, natural-language parsing, verifier error model, or non-arithmetic reasoning tasks were tested. The result is a bounded mechanism simulation over 20,000 synthetic tasks per condition and cannot support a paper-grade claim about LLM self-consistency voting.

## Claim scope

Synthetic arithmetic-ledger simulations show that ledger-filtered voting improves over answer-only majority when sampled errors are independent arithmetic or transcription slips, but internal self-consistency alone gives negligible gains when wrong ledgers are coherent and internally consistent. Prompt-grounded ledger verification is the mechanism that handles coherent omissions in this proxy.

## Why it stopped

Closed as no-paper useful signal: the evidence is synthetic/proxy and shows the self-consistency-only version is mixed, not publication-grade validation.

## Recommended next action

Run a bounded real-LLM follow-up on 500-1,000 ledger word problems comparing answer majority, internal-ledger voting, and prompt-grounded ledger verification with extraction failures and abstentions reported.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real LLM Ledger Vote With Prompt-Grounded Verification
- Success threshold: Prompt-grounded ledger verification improves non-abstained or coverage-adjusted accuracy by at least 5 percentage points over answer-only majority at K=5, with extraction failure below 20%, and internal self-consistency alone is separately characterized.
- Stop condition: Stop if parser/extraction failure exceeds 40%, if prompt-grounded verification does not beat answer majority by at least 2 percentage points at K=5 on the first 500 tasks, or if most errors are not ledger-verifiable.

## Evidence references

- Artifact root: `<local-path>/projects/ledger-self-consistency-vote-2cec5deb3656`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
