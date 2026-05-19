# Merkle-Trajectory Ledger to Detect Reward Hacking in Local PPO Agents

Status: `useful_signal`
Project ID: `merkle-trajectory-ledger-to-detect-reward-hacking-in-local-ppo-agents-08438f0bd9f8`
Run ID: `merkle-trajectory-ledger-to-detect-reward-hacking-in-local-ppo-agents-08438f0bd9f8-20260516T091307841161+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/26a54cf52b91

## What looked useful

Across 5 hackable seeds, PPO learned the exploit in 100% of evaluated episodes with 0% true success; the full ledger auditor achieved 100% recall with 0% false positives and every Merkle root rejected a tampered record. The aligned control had 100% true success and no exploit episodes. Reward-only logs had 0% detection recall in the hackable condition.

## Boundaries and scale limits

Evidence is limited to a handcrafted small MDP, 5 seeds per condition, 100 evaluation episodes per seed, and a compact local PPO implementation. It does not validate language-model PPO, learned reward models, human preference data, distributed training, external transparency anchoring, or adversarial agents aware of the auditor.

## Claim scope

In a deterministic local toy PPO environment, a Merkle-committed full trajectory ledger enabled offline detection of proxy-reward exploitation by preserving observations, actions, rewards, next observations, and episode metadata for true-objective audit.

## Why it stopped

No-paper closure: this run produced a useful local mechanism signal, but the evidence is toy/synthetic and not sufficient for a publication-grade claim about PPO reward-hacking detection in realistic agents.

## Recommended next action

Run a bounded deepen follow-up on a richer stochastic local reward-hacking benchmark with signed flat-log, reward-only, and field-ablation baselines before considering paper writing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Field-Ablated Merkle Trajectory Audits on Stochastic PPO Reward Hacking
- Success threshold: Merkle full-trajectory audit detects at least 90% of hacked episodes with no more than 5% false positives and materially outperforms reward-only and incomplete-log ablations across seeds.
- Stop condition: Stop if PPO does not learn the exploit in at least 50% of hackable-condition evaluation episodes after a calibrated training budget, or if incomplete baselines match full-ledger detection within 5 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-trajectory-ledger-to-detect-reward-hacking-in-local-ppo-agents-08438f0bd9f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
