# Medusa heads via tiny local fine-tune on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medusa-heads-via-tiny-local-fine-tune-on-gb10-4b7f660aa1ac`
Run ID: `medusa-heads-via-tiny-local-fine-tune-on-gb10-4b7f660aa1ac-20260629T110646253823+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d677fc24f5fe

## What looked useful

The frozen-head setup improved exact accepted prefix length over a shuffled-target control, but the gain came almost entirely from horizon 1. Horizon-2 through horizon-4 heads remained near chance accuracy and random-token cross-entropy even though the base model predicted those future positions well under teacher forcing.

## Boundaries and scale limits

Synthetic data only; tiny transformer only; no real tokenizer, real text corpus, production speculative decoder, tree attention, real LLM, joint model fine-tuning, or throughput benchmark. The result is a mechanism probe, not a full validation or full falsification of Medusa on real models.

## Claim scope

In a toy CUDA-local PyTorch experiment with a 421k-parameter causal transformer on a synthetic periodic sequence task, head-only fine-tuning of four independent Medusa-style MLP heads on frozen hidden states learned a strong horizon-1 auxiliary prediction head but did not learn useful horizons 2-4.

## Why it stopped

Bounded local mechanism test completed; evidence supports only horizon-1 head learning and early-falsifies the stronger toy claim that tiny independent head-only fine-tuning yields useful multi-token Medusa heads. This is proxy/toy evidence, not full real-LLM validation.

## Recommended next action

Stop this run as a no-paper useful signal; next test should compare recurrent/residual Medusa heads or partial unfreezing against the same frozen independent-head baseline on this toy task before scaling to a real small LM.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Recurrent or partially unfrozen Medusa heads for horizons 2-4
- Success threshold: At least one non-independent-head variant reaches horizon-2 accuracy >= 0.50 and mean exact accepted prefix length >= 1.30 while shuffled control remains near chance.
- Stop condition: Stop if horizons 2-4 remain below 0.10 accuracy after matched or larger local training budgets, or if gains only appear after unbounded model/data scaling.

## Evidence references

- Artifact root: `<local-path>/projects/medusa-heads-via-tiny-local-fine-tune-on-gb10-4b7f660aa1ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
