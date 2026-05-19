# Field-Ablated Merkle Trajectory Audits on Stochastic PPO Reward Hacking

Status: `useful_signal`
Project ID: `field-ablated-merkle-trajectory-audits-on-stochastic-ppo-r-d06cb953f3`
Run ID: `field-ablated-merkle-trajectory-audits-on-stochastic-ppo-r-d06cb953f3-20260516T092153023860+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/26a54cf52b91

## What looked useful

Field-ablated Merkle audits exposed concrete blind spots: full-field commitments detected all tested tamper modes, while schemas omitting reward/action/true-reward fields missed tampering isolated to those omitted fields.

## Boundaries and scale limits

Eight-seed controlled local test only; no neural PPO benchmark, RLHF reward model, large model training, distributed logging path, or real adversarial deployment was tested.

## Claim scope

In a toy tabular PPO environment with an explicit stochastic reward-hack action, trained PPO policies shifted from honest task completion to proxy-reward hacking, and Merkle trajectory commitments detected post-hoc tampering exactly when the tampered semantic fields were included in the committed schema.

## Why it stopped

Controlled small direct test supports the mechanism but is not publication-grade evidence; closing as no-paper useful signal rather than continuing without an explicit larger budget.

## Recommended next action

Run a bounded neural PPO reproduction in a standard Gymnasium-style environment with the same audit ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural PPO Field-Ablated Merkle Audit Reproduction
- Success threshold: Trained neural PPO has hack_episode_rate >= 0.80 and mean_true_return below the honest/control mean in at least 4 of 5 seeds; full-field Merkle audit detects 100% of tested tamper modes; at least two targeted field ablations miss the corresponding omitted-field tamper in 100% of seeds.
- Stop condition: Stop as negative if neural PPO does not learn the proxy hack in at least 4 of 5 seeds, if full-field audit fails any deterministic tamper check, or if ablations do not produce field-specific blind spots.

## Evidence references

- Artifact root: `<local-path>/projects/field-ablated-merkle-trajectory-audits-on-stochastic-ppo-r-d06cb953f3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
