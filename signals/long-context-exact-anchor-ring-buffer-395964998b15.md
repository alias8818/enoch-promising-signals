# Long-Context Exact Anchor Ring Buffer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `long-context-exact-anchor-ring-buffer-395964998b15`
Run ID: `long-context-exact-anchor-ring-buffer-395964998b15-20260604T062549179773+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/addd14148dd3

## What looked useful

At 1,048,576 tokens with a 2,048-token recent window and 512 anchor slots, anchor_ring achieved 1.000 accuracy on tail_anchored queries with 409.6x retained-token compression versus full cache, while sliding achieved 0.000 and random_anchor achieved 0.031. For uniform_old queries, anchor_ring fell to 0.031, showing the method only works when queried facts are inside the retained-anchor horizon.

## Boundaries and scale limits

No real transformer KV-cache patch, no trained model behavior, no RoPE/position validation, no learned anchor selection, no natural-language benchmark, and no serving-throughput measurement. Uniform arbitrary-old retrieval fails as context grows when the anchor budget is fixed.

## Claim scope

Synthetic oracle-anchor KV-cache retrieval with random normalized key/query vectors on one GB10 worker: a recent-window plus exact non-recent anchor ring preserves retrieval for queries inside the retained-anchor horizon at much lower retained-token count than full cache.

## Why it stopped

Synthetic proxy evidence supports the retained-anchor-horizon mechanism but early-falsifies the stronger arbitrary-long-context interpretation; this is not full validation or paper-ready evidence.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded action is a direct small-LM KV-cache implementation comparing full, sliding, anchor_ring, and random_anchor controls on synthetic prompt retrieval.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Direct KV-Cache Anchor Ring Retrieval
- Success threshold: Anchor_ring must exceed sliding and random_anchor by at least 20 percentage points on retained-horizon retrieval at 32k or longer context while preserving model correctness on short-context controls.
- Stop condition: Stop if the direct KV-cache implementation cannot retrieve retained anchors above random_anchor accuracy or if positional/cache mechanics break short-context correctness.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-exact-anchor-ring-buffer-395964998b15`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
