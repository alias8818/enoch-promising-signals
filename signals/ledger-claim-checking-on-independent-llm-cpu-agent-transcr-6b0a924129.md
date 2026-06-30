# Ledger Claim Checking on Independent LLM CPU-Agent Transcripts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `ledger-claim-checking-on-independent-llm-cpu-agent-transcr-6b0a924129`
Run ID: `ledger-claim-checking-on-independent-llm-cpu-agent-transcr-6b0a924129-20260521T234332748522+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Append-Only Evidence Ledger for CPU Agent Reliability: enoch://control-plane/projects/append-only-evidence-ledger-for-cpu-agent-reliability-8aaa751f4128/runs/append-only-evidence-ledger-for-cpu-agent-reliability-8aaa751f4128-20260521T225920908709+0000
- Parent run decision: Ledger-Enforced Claim Checking for Real CPU-Agent Runs: enoch://control-plane/projects/ledger-enforced-claim-checking-for-real-cpu-agent-runs-0cd50a7352/runs/ledger-enforced-claim-checking-for-real-cpu-agent-runs-0cd50a7352-20260521T233322793476+0000

## What looked useful

Full ledger checking reached 1.000 mean accuracy and 1.000 mean macro-F1 over 5000 examples; transcript-only baseline reached 0.6434 accuracy and 0.4572 macro-F1; random baseline reached 0.3336 accuracy and 0.3226 macro-F1; windowed ledger ablation dropped to 0.3650 accuracy and 0.3632 macro-F1.

## Boundaries and scale limits

5 fixed seeds, 1000 generated examples per seed, 24 tool facts and 16 distractors per transcript. No real LLM-agent transcript corpus, no natural claim extraction, no malformed or adversarial logs, and no human annotation.

## Claim scope

On a deterministic synthetic benchmark of independent CPU-agent transcripts with generated tool-observation ledgers and templated claims, scoped append-only ledger checking classifies supported, contradicted, and not-enough-information claims more accurately than transcript-only search and degrades under a history-window ablation.

## Why it stopped

Tier 2 synthetic benchmark supports the mechanism, but evidence remains no-paper because it lacks real independent LLM CPU-agent transcripts and natural claim extraction.

## Recommended next action

Run a real-transcript deepen test with manually audited tool-observation ledgers and natural claims; do not write a paper from this synthetic-only result.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transcript Ledger Claim Checking with Human-Audited Claims
- Success threshold: Ledger checker beats the real transcript-only baseline by >=0.15 macro-F1 and >=0.10 accuracy, with contradiction recall and not-enough-information recall both >=0.80.
- Stop condition: Stop negative if ledger macro-F1 gain is <0.05 or either contradiction recall or not-enough-information recall is <0.60 on the audited real-transcript set.

## Evidence references

- Artifact root: `<local-path>/projects/ledger-claim-checking-on-independent-llm-cpu-agent-transcr-6b0a924129`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
