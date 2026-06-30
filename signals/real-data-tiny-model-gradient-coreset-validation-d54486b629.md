# Real-data tiny-model gradient coreset validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-data-tiny-model-gradient-coreset-validation-d54486b629`
Run ID: `real-data-tiny-model-gradient-coreset-validation-d54486b629-20260602T231810793629+0000`

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

- Parent run decision: Gradient Coreset Selection for Tiny Model Home Training: enoch://control-plane/projects/gradient-coreset-selection-for-tiny-model-home-training-7592a0240576/runs/gradient-coreset-selection-for-tiny-model-home-training-7592a0240576-20260602T191454673702+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b67010670af1

## What looked useful

Tier 1 real-data run shows gradient coresets preserve full-batch update effects far better than random subsets at small k. At fullbatch_step25_k16, mean test accuracy update gap was 0.00145 for coreset versus 0.15815 for random; at k64, relative gradient L2 error was 0.2338 versus 2.0579 for random.

## Boundaries and scale limits

Single small real dataset; tiny MLP; one-step gradient/update approximation; no language model, no large-corpus training, no optimizer-through-training result, and no architecture or dataset robustness claim.

## Claim scope

On UCI optical handwritten digits with a 2410-parameter NumPy 64-32-10 MLP, greedy least-squares gradient coreset subsets selected from 768 candidates approximate full-batch gradients and one-step loss/accuracy effects substantially better than random subsets across 5 seeds and k=16,32,64,128.

## Why it stopped

The mechanism is supported on one small real dataset, but the evidence is too narrow for publication-grade claims.

## Recommended next action

Archive this as a no-paper useful signal and run a bounded second-dataset confirmation before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Second-dataset gradient coreset confirmation for tiny neural models
- Success threshold: At k<=64, coreset mean relative L2 error improves by at least 50% over random and test loss/accuracy update gaps remain at least 50% below random across at least 5 seeds.
- Stop condition: Stop if coreset advantage over random falls below 25% on relative L2 error or downstream update gaps on the second dataset.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-tiny-model-gradient-coreset-validation-d54486b629`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
