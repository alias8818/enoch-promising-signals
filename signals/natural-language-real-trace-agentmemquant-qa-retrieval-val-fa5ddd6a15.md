# Natural-language real-trace AgentMemQuant QA retrieval validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `natural-language-real-trace-agentmemquant-qa-retrieval-val-fa5ddd6a15`
Run ID: `natural-language-real-trace-agentmemquant-qa-retrieval-val-fa5ddd6a15-20260527T012513257826+0000`

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

- Parent run decision: AgentMemQuant: enoch://control-plane/projects/agentmemquant-fec115a9a6d2/runs/agentmemquant-fec115a9a6d2-20260525T161951437822+0000
- Parent run decision: Real-trace AgentMemQuant retrieval validation: enoch://control-plane/projects/real-trace-agentmemquant-retrieval-validation-47c8be6334/runs/real-trace-agentmemquant-retrieval-validation-47c8be6334-20260526T185431354120+0000

## What looked useful

The top-64 quantized IDF sketch passed all fixed-seed thresholds: mean Recall@5 0.6540, mean relative Recall@5 vs best full BM25/TF-IDF/hybrid baseline 0.9190, mean compression 5.50x, and mean answer-support@5 0.6613. Top-16/top-8 failed recall, top-frequency controls failed, unquantized float-IDF missed compression, and random top-64 was a strong but not all-seed-passing control.

## Boundaries and scale limits

Tier 2 local retrieval-only validation: 3 seeds, 3000 chunks and 500 auto-derived QA pairs per seed, 1500 total QA pairs. Questions are deterministic natural-language formulations from real trace facts rather than independent human labels. No neural dense embedding baseline, no live downstream answer generation, no production memory serving, no multi-session aging or contradiction handling.

## Claim scope

On local real Codex/Enoch trace chunks with deterministic natural-language QA-style labels, AgentMemQuant quantized top-IDF sketches at top-64 retained a mean 91.9% of the best full lexical baseline Recall@5 across seeds 47/48/49 while reducing retrieval-state storage by 5.50x and losing only 2.53 absolute answer-support@5 points.

## Why it stopped

Tier 2 direct retrieval evidence supports the bounded compression/retrieval mechanism, but the evidence is not publication-grade because labels are auto-derived and deterministic, the strongest comparison is lexical rather than neural dense retrieval, and downstream QA generation was not tested.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded deepen step should run live answer generation from retrieved evidence on held-out natural-language memory questions and include a neural embedding baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live answer-generation validation for AgentMemQuant real-trace memory retrieval
- Success threshold: Across at least 500 held-out questions, AgentMemQuant top-64 must achieve >=95% of the best full baseline answer accuracy, >=90% of the best baseline Recall@5, >=4x storage compression, and <=5% retrieval-plus-answering latency overhead.
- Stop condition: Stop early if the first 150 held-out questions show AgentMemQuant below 85% relative Recall@5 or more than 10 absolute points answer-accuracy loss versus the best full baseline.

## Evidence references

- Artifact root: `<local-path>/projects/natural-language-real-trace-agentmemquant-qa-retrieval-val-fa5ddd6a15`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
