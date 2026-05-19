# Calibrated Auxiliary Early-Exit Draft for Speculative Decoding

Status: `useful_signal`
Project ID: `calibrated-auxiliary-early-exit-draft-for-speculative-deco-f71fb85632`
Run ID: `calibrated-auxiliary-early-exit-draft-for-speculative-deco-f71fb85632-20260515T202402593239+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/f8aa642cf3d5

## What looked useful

Calibrated early exit achieved 0.8133 target-match at 0.8268 compute fraction and beat fixed layer 5 match by 35.6 percentage points at similar compute, but its estimated 4-token speculative speedup was 0.8011x. The best nontrivial threshold sweep reached 0.9835 match with 0.9849 compute and still only 0.9794x estimated speedup.

## Boundaries and scale limits

Single GPT-2-class pretrained model, 2,457 calibration tokens, 3,402 test tokens, greedy target-token match proxy, layer-count compute estimate, tied LM head auxiliary exits rather than separately trained auxiliary heads, no wall-clock early-exit serving kernel.

## Claim scope

Tier-1 small direct test on distilgpt2 with WikiText-2 next-token positions: confidence calibration can select more reliable intermediate exits than fixed layers, but the selected exits are not cheap enough to yield estimated speculative decoding speedup.

## Why it stopped

Early direct test supports calibration as a selector but falsifies the practical speed threshold under the tested tied-head early-exit setup; no nontrivial calibrated threshold exceeded 1.0x estimated full-greedy speed.

## Recommended next action

Stop this as no-paper Tier-1 evidence; only pursue a bounded deepen run if training real auxiliary heads and measuring wall-clock speculative throughput is in scope.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Train Real Auxiliary Exit Heads for Early-Exit Speculative Drafting
- Success threshold: At least one nontrivial policy must achieve target-match >= 0.75, draft compute fraction <= 0.60, non-final exit fraction >= 0.50, and measured throughput >= 1.10x full greedy decoding on held-out text.
- Stop condition: Stop if trained heads cannot reach target-match >= 0.75 below 0.60 compute fraction, or if wall-clock speculative throughput remains <= 1.0x after kernel/runtime overhead is included.

## Evidence references

- Artifact root: `<local-path>/projects/calibrated-auxiliary-early-exit-draft-for-speculative-deco-f71fb85632`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
