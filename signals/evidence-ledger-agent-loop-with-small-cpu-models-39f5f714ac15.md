# Evidence-ledger agent loop with small CPU models

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-agent-loop-with-small-cpu-models-39f5f714ac15`
Run ID: `evidence-ledger-agent-loop-with-small-cpu-models-39f5f714ac15-20260604T210909776239+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48518d91158f

## What looked useful

Main 200-task run: direct supported accuracy 0.375 versus ledger 1.000, a +0.625 gain, with mean latency rising from 5.18 ms to 7.57 ms per task. A k=1 retrieval-depth control removed the gain, showing the ledger needs recall of current evidence and is not merely a stronger extractor. A high-conflict control showed direct 0.185 versus ledger 1.000 supported accuracy.

## Boundaries and scale limits

This run did not use a real small CPU language model, real corpora, paraphrased evidence, multi-hop tasks, noisy source metadata, or long-horizon tool use. The strongest result is synthetic and mechanism-level, not publication-grade validation of small CPU LLM agents.

## Claim scope

On a synthetic stale-evidence fact lookup benchmark with weak CPU-only lexical retrieval and extraction components, an evidence-ledger loop that records source, timestamp, support, and conflict entries improved supported answer accuracy over a single-pass direct agent when current supporting evidence was retrievable beyond the top stale snippet.

## Why it stopped

Bounded synthetic evidence supports the ledger mechanism but is not direct/full evidence for real small CPU model agent loops.

## Recommended next action

Stop this run as no-paper useful signal; next run should replace lexical extraction with a real small CPU language model or CPU-friendly NLI classifier on a semi-real stale/conflicting evidence QA benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence-ledger loop with a real small CPU model on stale-evidence QA
- Success threshold: At least +0.10 supported accuracy over a direct small-model baseline across 200 or more held-out tasks, with no more than 2x mean latency and an ablation showing the gain depends on ledger conflict handling.
- Stop condition: Stop if ledger supported accuracy improves by less than 0.05, if gains vanish under retrieval-depth/source-trust ablation, or if CPU latency exceeds 2x baseline without accuracy benefit.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-agent-loop-with-small-cpu-models-39f5f714ac15`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
