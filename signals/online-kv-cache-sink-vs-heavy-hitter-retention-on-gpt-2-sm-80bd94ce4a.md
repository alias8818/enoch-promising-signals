# Online KV-Cache Sink-vs-Heavy-Hitter Retention on GPT-2-Small-Class Long Contexts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `online-kv-cache-sink-vs-heavy-hitter-retention-on-gpt-2-sm-80bd94ce4a`
Run ID: `online-kv-cache-sink-vs-heavy-hitter-retention-on-gpt-2-sm-80bd94ce4a-20260602T203903721220+0000`

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

- Parent run decision: Attention-Sink Bounded KV Eviction: enoch://control-plane/projects/attention-sink-bounded-kv-eviction-808f27a739ff/runs/attention-sink-bounded-kv-eviction-808f27a739ff-20260602T121813606155+0000
- Parent run decision: Compare Attention-Sink Retention Against Heavy-Hitter KV Eviction: enoch://control-plane/projects/compare-attention-sink-retention-against-heavy-hitter-kv-e-82a0b2cf5d/runs/compare-attention-sink-retention-against-heavy-hitter-kv-e-82a0b2cf5d-20260602T164000940663+0000

## What looked useful

Medium confirmation found dense mean NLL 3.5373. At budget 64, recent-only delta NLL was +4.8616, sink+recent +0.5915, and heavy-hitter+recent +0.4050. At budget 128, recent-only delta NLL was +3.6057, sink+recent +0.3619, and heavy-hitter+recent +0.2006. Sink+heavy-hitter matched heavy-hitter alone; sink retention rate was 0.9971, indicating heavy-hitter scores already captured sink tokens.

## Boundaries and scale limits

Single GPT-2-small model, WikiText-2 only, 12 sampled sequences, 512 scored tokens, fp16 inference, GPT-2 learned absolute-position limit; no production serving latency study, no >1024 context model, no larger-model robustness, and no generation-quality or human evaluation.

## Claim scope

On GPT-2-small streamed over 12 fixed-seed WikiText-2 test sequences of 512 scored tokens, sink+recent and heavy-hitter+recent KV-cache retention preserve next-token NLL far better than recent-only at 64-token and 128-token cache budgets. Heavy-hitter+recent outperforms sink+recent, and explicit sink tokens add no quality benefit to heavy-hitter retention because the online heavy-hitter scores already retain sink tokens.

## Why it stopped

Tier-2 direct medium evidence supports the scoped mechanism but is not broad or robust enough for publication-grade claims.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded deepen test should repeat the same online pruning evaluation at 1024 scored tokens with more WikiText-2/OpenWebText sequences and sink-count ablations.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: 1024-token GPT-2-small KV retention robustness with sink-count ablations
- Success threshold: Heavy-hitter+recent mean delta NLL versus dense is at least 0.10 lower than sink+recent at two or more budgets, recent-only remains clearly worse, and sink+heavy-hitter provides no more than 0.02 NLL improvement over heavy-hitter alone.
- Stop condition: Stop if heavy-hitter+recent fails to beat sink+recent by 0.05 mean delta NLL at every tested budget or if explicit sink tokens improve heavy-hitter by more than 0.05 mean delta NLL, falsifying the redundancy mechanism.

## Evidence references

- Artifact root: `<local-path>/projects/online-kv-cache-sink-vs-heavy-hitter-retention-on-gpt-2-sm-80bd94ce4a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
