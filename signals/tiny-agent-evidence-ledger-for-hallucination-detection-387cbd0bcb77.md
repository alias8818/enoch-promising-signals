# Tiny Agent Evidence Ledger for Hallucination Detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tiny-agent-evidence-ledger-for-hallucination-detection-387cbd0bcb77`
Run ID: `tiny-agent-evidence-ledger-for-hallucination-detection-387cbd0bcb77-20260529T124453457296+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/6788e13f97b2

## What looked useful

Ledger-aware verification reached F1 1.000 on 1,507 unsupported/contradicted cases while two answer-only baselines had F1 0.000; however, a strong post-hoc retrieval oracle also reached F1 1.000, so the result supports a compact trace-level mechanism but not a broad novelty or paper claim.

## Boundaries and scale limits

Synthetic closed-world corpus only; no real LLM traces, human labels, open-domain retrieval, paraphrase robustness, multi-hop evidence, adversarial ledgers, or large-corpus latency validation.

## Claim scope

In a deterministic synthetic QA trace benchmark with 40 source facts and 2,000 generated examples, a tiny evidence ledger using cited document id and cited quote detects missing, contradicted, and wrong-subject citations that answer-only heuristics miss, and matches a strong closed-world retrieval oracle.

## Why it stopped

Proxy/synthetic useful signal only: the experiment directly tested controlled generated traces, not real hallucination detection in deployed agents, and the ledger tied rather than beat a closed-world retrieval oracle.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a real-agent trace benchmark with logged evidence ledger fields and human or verifier labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Evidence Ledger Benchmark
- Success threshold: Ledger-aware verification improves F1 by at least 0.10 over answer-only baselines, stays within 0.03 F1 of post-hoc retrieval verification, and reduces verification context or latency by at least 30% on the same trace set.
- Stop condition: Stop if ledger-aware verification falls below answer-only F1, has more than 10% absolute false-positive rate on supported paraphrases, or offers no measurable cost/context reduction versus post-hoc retrieval.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-for-hallucination-detection-387cbd0bcb77`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
