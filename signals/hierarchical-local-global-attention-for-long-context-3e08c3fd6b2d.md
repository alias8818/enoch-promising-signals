# Hierarchical local-global attention for long context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-local-global-attention-for-long-context-3e08c3fd6b2d`
Run ID: `hierarchical-local-global-attention-for-long-context-3e08c3fd6b2d-20260527T114721090513+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/904c3dfc2ffb

## What looked useful

Landmark-routed hierarchical attention recovered salient remote targets with far fewer candidates than dense attention, reaching 92.6% top-1 at 4096 tokens with 15.6% of dense candidates, but ordinary remote-key retrieval stayed low at 21.5%. Mean block summaries and local-only attention failed exact remote retrieval.

## Boundaries and scale limits

No model training, no learned summaries, no language-model perplexity, no GPT-2-small-class baseline, and no optimized sparse/GPU kernel measurements. Wall-clock timings reflect a Python/NumPy prototype, not deployable attention performance.

## Claim scope

Synthetic NumPy proxy tests of local-only, mean-summary, and landmark-routed hierarchical attention on exact remote-key retrieval at 2048-4096 tokens.

## Why it stopped

Proxy/mechanism evidence is mixed and not paper-ready: the method works for salient represented targets but fails for ordinary remote targets without learned routing evidence.

## Recommended next action

Run a bounded learned-landmark transformer probe on synthetic associative retrieval; stop if ordinary remote-key recovery remains below 80% while using no more than 25% of dense candidates.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Learned block landmarks for ordinary remote-key retrieval
- Success threshold: Hierarchical learned-landmark model reaches at least 80% ordinary remote-key retrieval and at least 95% of dense baseline task accuracy while using no more than 25% of dense attention candidates/FLOPs.
- Stop condition: Stop as a negative if learned landmarks stay below 80% ordinary remote-key retrieval after matched training budget or require more than 25% dense candidate/FLOP use to close the gap.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-local-global-attention-for-long-context-3e08c3fd6b2d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
