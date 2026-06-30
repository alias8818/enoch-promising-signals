# Real Small-Model Evidence-Led Tool Loop on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-small-model-evidence-led-tool-loop-on-cpu-22120d32dd`
Run ID: `real-small-model-evidence-led-tool-loop-on-cpu-22120d32dd-20260608T124011467241+0000`

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

- Parent run decision: Evidence-Led Agent Loop for Small Tool-Use Models on CPU: enoch://control-plane/projects/evidence-led-agent-loop-for-small-tool-use-models-on-cpu-d38f88b02d09/runs/evidence-led-agent-loop-for-small-tool-use-models-on-cpu-d38f88b02d09-20260608T061100951251+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c21b4dafbe61

## What looked useful

A real small CPU-run model showed a large paired gain from an evidence-led tool loop on controlled local facts: 11 evidence-over-direct wins, 0 losses, 1 tie; target evidence was retrieved in top 3 for all 12 model-generated queries.

## Boundaries and scale limits

Single small instruct model, synthetic short-fact corpus, lexical retrieval, short-span answers, deterministic decoding, no real web/search API, no noisy real corpus, no multi-hop tasks, no adversarial evidence, and no serving-load measurement.

## Claim scope

In a 12-item controlled local-document QA benchmark with synthetic novel facts and distractors, Qwen/Qwen2.5-0.5B-Instruct running on CPU improved from 0/12 direct-answer accuracy to 11/12 evidence-loop accuracy when it generated a search query, retrieved top-3 lexical evidence, and answered from that evidence.

## Why it stopped

Tier 1 direct controlled evidence supports the mechanism but is small, synthetic, and not publication-grade; close as no-paper useful signal rather than continue scaling inside this run.

## Recommended next action

Run a medium confirmation benchmark with at least 100 held-out real-document short-answer questions, stronger distractors, and direct/RAG/oracle-retrieval ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Real-Document Evidence-Loop Confirmation for Small CPU Models
- Success threshold: Evidence-loop answer accuracy exceeds direct-answer accuracy by at least 25 percentage points, target evidence appears in top 3 for at least 80 percent of model-generated queries, and the improvement persists under one prompt or model variant.
- Stop condition: Stop if evidence-loop accuracy improves over direct by less than 10 percentage points, target evidence top-3 retrieval falls below 60 percent, or most wins are attributable to oracle-like corpus templating rather than robust query generation.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-model-evidence-led-tool-loop-on-cpu-22120d32dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
