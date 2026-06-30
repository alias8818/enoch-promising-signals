# Quantized Evidence Ledger for Small Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-evidence-ledger-for-small-agents-508641cebb21`
Run ID: `quantized-evidence-ledger-for-small-agents-508641cebb21-20260604T190646972310+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/bc4eb80e5e73

## What looked useful

Int8 evidence-vector quantization appears viable as a compact small-agent ledger mechanism in a bounded synthetic retrieval task; binary sign quantization was much smaller but lost more retrieval and answer quality.

## Boundaries and scale limits

Synthetic vectors and a simple verifier only; no real LLM agent, real embeddings, natural-language evidence extraction, external retrieval, prompt-token accounting, or long-horizon workflow was tested.

## Claim scope

On a deterministic synthetic claim-verification benchmark with 5 trials, 3,600 evidence snippets per trial, and 1,440 balanced queries per trial, an int8 quantized evidence ledger preserved float32 answer accuracy within 0.28 percentage points while using 25.39% of float32 vector storage and retaining retrieval performance above recency/random controls.

## Why it stopped

Synthetic/proxy evidence supports the mechanism only partially and is not a full validation of small-agent behavior.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the ledger variants into a real small-agent QA/fact-checking harness with fixed context budgets and citation metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent int8 evidence ledger validation under fixed context budgets
- Success threshold: Int8 ledger achieves at least 95% of float32 task accuracy and citation recall, beats recency/no-ledger baselines by at least 5 percentage points on task accuracy or citation recall, and uses no more than 30% of float32 ledger storage.
- Stop condition: Stop negative if int8 loses more than 5% task accuracy or citation recall versus float32, or fails to beat recency/no-ledger baselines on direct real-agent metrics.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-evidence-ledger-for-small-agents-508641cebb21`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
